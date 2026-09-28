def answer_question(question: str) -> str:
    """
    Answer a student's question.
    """

    if not question or not question.strip():
        return "Please enter a question."

    question = question.strip()

    return (
        f"Answer to your question:\n\n"
        f"{question}\n\n"
        "Please provide more details if you need a step-by-step explanation."
    )