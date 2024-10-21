from crewai import Crew, Process
from agents import Resource_Generator, Post_Creator, Platform_Adapter
from tasks import resource_task, write_task, platform_task


# Forming the crew with the necessary agents and tasks
crew = Crew(
    agents=[
        Resource_Generator,
        Post_Creator,
        Platform_Adapter
    ],
    tasks=[resource_task, write_task, platform_task],
    process=Process.sequential  # Executes tasks in the defined sequence
)

# Executing the tasks
result = crew.kickoff(inputs = {
    "criteria": "implementing AI technologies in agricultural practices",
    "topic": "AI in Agriculture",
    "tone": "informative",
    "platform": "LinkedIn"  # You can change this to any other platform as needed
})

# Print the output
print(result)
