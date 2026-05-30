from dotenv import load_dotenv
load_dotenv()

from tools import (
    skill_gap_analyzer,
    project_recommender,
    interview_questions
)

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.1
)


def career_agent(skills, goal):

    missing_skills = skill_gap_analyzer(
        skills,
        goal
    )

    projects = project_recommender(goal)

    questions = interview_questions(goal)

    prompt = f"""
You are an AI Career Mentor Agent.

Student Skills:
{skills}

Career Goal:
{goal}

Missing Skills:
{missing_skills}

Recommended Projects:
{projects}

Interview Questions:
{questions}

IMPORTANT:

Use ONLY the missing skills, projects, and interview questions provided.

Keep the response under 300 words.

Generate exactly in this format:

## Skill Analysis

Current Skills:
(List the student's skills)

Missing Skills:
(List the missing skills)

## 6-Month Roadmap

Month 1:
Month 2:
Month 3:
Month 4:
Month 5:
Month 6:

## Recommended Projects

(Display the provided projects as a numbered list)

## Interview Questions

(Display the provided interview questions as a numbered list)

Do not create new interview questions.
Do not add extra sections.
Keep the answer concise and practical.
"""

    result = llm.invoke(prompt)

    return result.content