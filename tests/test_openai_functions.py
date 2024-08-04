import json

import pytest
from dotenv import load_dotenv
from openai import OpenAI

from orango import Sandbox

load_dotenv()


@pytest.fixture(scope="module")
def openai_client():
    return OpenAI()

def test_run_conversation(openai_client):
    tool = Sandbox(type='python')
    print(tool)
    messages = [{"role": "user", "content": "What is the 10th number of the fibonacci series?"}]
    tools = [tool.get_openai_function_spec()]
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    
    if tool_calls:
        available_functions = {
            **tool.get_openai_functions(),
        }
        messages.append(response_message)
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(**function_args)


            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_response,
            })
        second_response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )

        assert "55" in second_response.choices[0].message.content  # Assuming 55 is part of the response
