from ai_client import generate_text


def explain_concept(topic: str) -> str:
    """
    Explain a concept in a simple, beginner-friendly way.
    """

    prompt = f"""
You are EduGenie, an AI learning assistant.

Explain the following topic to a student:

Topic: {topic}

Give the answer in this format:

1. Simple definition
2. Easy explanation
3. Important points
4. Real-world example
5. Short example if applicable
6. Quick recap

Use simple language and make the explanation easy for a student to understand.
"""

    return generate_text(prompt)