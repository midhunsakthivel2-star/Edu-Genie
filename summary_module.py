def summarize_text(text: str) -> str:
    """
    Create a simple summary from the given text.
    """

    if not text or not text.strip():
        return "Please provide some text to summarize."

    text = text.strip()

    # Split text into sentences
    sentences = text.replace("\n", " ").split(".")
    sentences = [s.strip() for s in sentences if s.strip()]

    # Keep first few sentences as a simple summary
    if len(sentences) <= 3:
        return ". ".join(sentences) + "."

    summary = ". ".join(sentences[:3]) + "."

    return summary