from crewai import Task
from agents import researcher, writer, seo_expert, reviewer
from tools import search_tool

# Research Task
research_task = Task(
    description='''
        Research {topic}.
        Focus on skincare, salons, social media and personalization.
    ''',
    expected_output="Bullet points with facts and trends.",
    agent=researcher
)

# Writing Task
writing_task = Task(
    description='''
        Write a 600-800 word article using the research.
        Include introduction, sections and conclusion.
    ''',
    expected_output="A well-structured article in markdown.",
    agent=writer,
    context=[research_task]
)

# SEO Task
seo_task = Task(
    description='''
        Optimize the article for SEO.
        Improve headings, keywords and readability.
    ''',
    expected_output="SEO-optimized version of the article.",
    agent=seo_expert,
    context=[writing_task]
)

# Review Task
review_task = Task(
    description='''
        Review the article for any factual accuracy and clarity.
        Improve wording if needed.
    ''',
    expected_output="Final polished article",
    agent=reviewer,
    context=[seo_task]
)