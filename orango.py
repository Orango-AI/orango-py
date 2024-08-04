import os

import requests
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import StructuredTool, tool
from langchain_core.tools import ToolException


class OrangoException(Exception):
    def __init__(self, result, stderr):
        self.result = result
        self.stderr = stderr
        super().__init__(self.stderr)

class OrangoExecutionResult:
    def __init__(self, success, result, stdout, stderr, session_id):
        self.success = success
        self.result = result
        self.stdout = stdout
        self.stderr = stderr
        self.session_id = session_id





class Sandbox:
    def __init__(self, type:str = 'python', base_url: str = None, api_key: str = None, template_id: str = None):
        self.base_url =  base_url or os.getenv('ORANGO_BASE_URL') or 'https://orango.ai/api/v1'
        self.api_key = api_key or os.getenv('ORANGO_APIKEY')
        self.template_id = template_id
        self.session_id = None
        self.type = type
        if not self.api_key:
            raise ValueError("API key must be provided either as an argument or through the ORANGO_APIKEY environment variable.")


    def clean_code(self, code: str) -> str:
        return code
    

    

    def exec(self, code: str) -> OrangoExecutionResult:
        print(3,self.base_url)

        headers = {'Authorization': f'Bearer {self.api_key}'}
        code = self.clean_code(code)
        payload = {
            'code': code,
            'language': self.type,
            'env': {},
            'sessionId': self.session_id,
        }
        if self.template_id:
            payload['templateId'] = self.template_id
        response = requests.post(f'{self.base_url}/execute', json=payload, headers=headers)
        response_data = response.json()

        self.session_id = response_data.get('sessionId')

        if response_data.get('stderr'):
            raise OrangoException(response_data, response_data.get('stderr'))

        return OrangoExecutionResult(
            success=response_data.get('success'),
            result=response_data.get('result'),
            stdout=response_data.get('stdout'),
            stderr=response_data.get('stderr'),
            session_id=response_data.get('sessionId')
        )
    
    def get_langchain_tool(self):

        print(1,self.base_url)

        def tool_fn(code: str) -> str:
            try:
                print(2,self.base_url)
                return self.exec(code).result
            except OrangoException as e:
                print(4,e)
                raise ToolException(e.stderr)
            
        class LangchainSandboxToolInput(BaseModel):
            code: str = Field(description=f"{self.type} code to execute in the sandbox without the language specifier or code block delimiters.")


        return StructuredTool.from_function(
            func=tool_fn,
            args_schema=LangchainSandboxToolInput,
            name=f"execute_{self.type}_code",
            description=f"Execute {self.type} code in the sandbox and return the result.",
        )
    
    def get_openai_function_spec(self):
        return {
            "type": "function",
            "function": {
                "name": f"execute_{self.type}_code",
                "description": f"Execute {self.type} code in the sandbox and return the result.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "code": {
                            "type": "string",
                            "description": f"{self.type} code to execute in the sandbox without the language specifier or code block delimiters.",
                        }
                    },
                    "required": ["code"],
                },
            },
        }
    def get_openai_functions(self):

        def tool_fn(code: str) -> str:
            try:
                return str(self.exec(code).result)
            except OrangoException as e:
                raise e.stderr

        return {
            f"execute_{self.type}_code": tool_fn
        }

    def close(self):
        # Optionally, close the sandbox or clean up resources
        pass








