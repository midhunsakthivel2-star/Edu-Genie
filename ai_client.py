import os
from dotenv import load_dotenv

load_dotenv()


def generate_text(prompt: str) -> str:
    """
    Generate a text response for EduGenie.

    If no AI API key is configured, return a simple
    local response so the application can still run.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    # Run without an API key
    if not api_key:
        return (
            "AI service is not configured yet.\n\n"
            f"Your question was:\n{prompt}\n\n"
            "Please add OPENAI_API_KEY to your .env file "
            "to enable AI-generated answers."
        )

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)

        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-5-mini"),
            input=prompt,
        )

        return response.output_text

    except Exception as e:
        return f"AI service error: {str(e)}"