import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from deepagents import create_deep_agent
from langchain_community.tools import DuckDuckGoSearchRun

# 1. Load Environment Variables
load_dotenv()

# 2. Load the Context Engineering Document
with open("context.md", "r", encoding="utf-8") as file:
    engineered_context = file.read()

# 3. Define the System Prompt
# This combines the dynamic role assignment with the strict context rules.
system_prompt = f"""
You are executing a workflow-driven AI agent task.
Below is your engineered context and operational guardrails. You must adhere to them strictly.

{engineered_context}
"""

# 4. Initialize LLM and Tools
llm = ChatGroq(
    model="openai/gpt-oss-120b", 
    temperature=0.2
)
search_tool = DuckDuckGoSearchRun()

# 5. Create the Deep Agent
research_agent = create_deep_agent(
    model=llm,
    tools=[search_tool],
    system_prompt=system_prompt
)

print("Modular Deep Agent successfully initialized with external context!")

# To test the agent, you can use:
# response = research_agent.invoke({"messages": [("user", "Hello! Can you research the latest trends in edge computing?")]})
# print(response["messages"][-1].content)