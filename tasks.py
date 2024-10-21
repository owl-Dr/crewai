from crewai import Task
from tools import tool
from agents import Resource_Generator, Post_Creator, Platform_Adapter

# Resource generation task
resource_task = Task(
    description=(
        "Generate a detailed list of resources required for {criteria}."
        "Include tools, materials, and any relevant contacts."
        "Your final output should provide clear guidance on the necessary resources."
    ),
    expected_output='A comprehensive list of resources for the specified project.',
    tools=[tool],
    agent=Resource_Generator,
)

# Writing task with specific tone
write_task = Task(
    description=(
        "Create a well-crafted post on {topic}."
        "The post should match the desired tone of {tone} and convey the message effectively."
        "It should be engaging, informative, and tailored to the target audience."
    ),
    expected_output='A 3 paragraph post on {topic} tailored to the specified tone.',
    tools=[tool],
    agent=Post_Creator,  # Using a lambda to instantiate with tone

)

# Platform adaptation task
platform_task = Task(
    description=(
        "Adapt the post for {platform}."
        "Ensure that it follows the best practices for engagement and formatting."
        "Highlight the key elements to attract the target audience on this platform."
    ),
    expected_output='A formatted post ready for publishing on {platform}.',
    tools=[tool],
    agent = Platform_Adapter,
    async_execution = False,
    output_file='post.md',
)

