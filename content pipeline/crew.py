from crewai import Crew
from agents import researcher, writer, seo_expert, reviewer
from tasks import research_task, writing_task, seo_task, review_task

# Create Crew
crew = Crew(
    agents=[researcher, writer, seo_expert, reviewer],
    tasks=[research_task, writing_task, seo_task, review_task],
    process="sequential",
    verbose=True
)

inputs = {
    'topic': 'current application of AI in beauty industry.'
}

result = crew.kickoff(inputs=inputs)
print(result)
