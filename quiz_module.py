def generate_quiz(topic: str, num_questions: int = 5):
    if not topic or not topic.strip():
        return []

    questions = []

    for i in range(1, num_questions + 1):
        questions.append({
            "question": f"{topic} - Question {i}",
            "options": [
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],
            "answer": "Option A"
        })

    return questions