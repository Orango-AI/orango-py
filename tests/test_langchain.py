import pytest
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.llms import OpenAI

from orango import Sandbox

load_dotenv()



@pytest.fixture(scope="module")
def react_agent_executor():
    tools = [Sandbox(type='python').get_langchain_tool()]
    print(tools)
    react_agent = create_react_agent(
        llm=OpenAI(),
        tools=tools,
        prompt=hub.pull("hwchase17/react"),
    )
    return AgentExecutor(agent=react_agent, tools=tools, verbose=True, handle_parsing_errors=True)

def test_fibonacci_series(react_agent_executor):
    response = react_agent_executor.invoke({"input": "What is the 10th number of the fibonacci series?"})
    print(response)
    assert "55" in response['output']  # Assuming 55 is part of the response for the 10th Fibonacci number
