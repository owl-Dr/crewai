from crewai import Agent
from textwrap import dedent
import os
from dotenv import load_dotenv
from tools import tool

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI  


llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

Resource_Generator = Agent(
        role="Resource Generation Expert",
        backstory=dedent("""You are an expert at creating helpful and relevant resources for various situations."""),
        goal=dedent("""Given a set of criteria, generate a detailed list of resources, tools, or materials required to address the current scenario effectively."""),
        tools=[tool],
        allow_delegation=True,
        verbose=False,
        llm=llm,
    )

Post_Creator = Agent(
        role="Expert Content Creator",
        backstory=dedent("""You are a skilled writer who tailors your tone based on user preferences to craft impactful posts."""),
        goal=dedent(f"""Given the required tone, create a well-crafted post that conveys the message effectively, adhering to the desired style and tone."""),
        tools=[tool],
        allow_delegation=True,
        verbose=False,
        llm=llm,
    )

Platform_Adapter = Agent(
        role="Platform Adaptation Expert",
        backstory=dedent("""You are an expert in adjusting content to fit the unique requirements and format of various social media or publishing platforms."""),
        goal=dedent(f"""Given a post, you will format and adapt it so that it is optimized for posting on platform. Ensure it follows the best practices for engagement and format for the chosen platform."""),
        tools=[tool],
        allow_delegation=False,
        verbose=False,
        llm=llm,
    )
