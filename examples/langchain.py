from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.llms import OpenAI

from orango import LangchainSandboxTool as SandboxTool

load_dotenv()


tools=[SandboxTool(type='python')]
react_agent = create_react_agent(
    llm=OpenAI(),
    tools=tools,
    prompt=hub.pull("hwchase17/react"),
)

react_agent_executor = AgentExecutor(agent=react_agent, tools=tools, verbose=True, handle_parsing_errors=True)

react_agent_executor.invoke({"input": "What is the 10th number of the fibonacci series?"})