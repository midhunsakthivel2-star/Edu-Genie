def explanation_prompt(topic):
    return f"""
Explain the following topic in simple and easy-to-understand language.

Topic: {topic}

Give:
1. Simple definition
2. Main points
3. Easy example
4. Short conclusion

Keep the explanation suitable for students.
"""


def summary_prompt(text):
    return f"""
Summarize the following educational content in simple language.

Content:
{text}

Give the important points in a short and clear format.
"""


def question_answer_prompt(question, context=""):
    return f"""
Answer the following question clearly and simply.

Context:
{context}

Question:
{question}

Give a short and accurate answer.
"""