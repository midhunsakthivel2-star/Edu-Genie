from ai_client import generate_text


def get_learning_recommendations(
    topic: str,
    level: str = "beginner",
    weeks: int = 6
) -> str:
    prompt = f"""
Create a {weeks}-week learning path for the topic: {topic}.

Student level: {level}

Include:
1. Weekly learning goals
2. Important concepts
3. Practice activities
4. Recommended mini-projects
5. A final revision plan

Keep the explanation simple and practical.
"""

    return generate_text(prompt)