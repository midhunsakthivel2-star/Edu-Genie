from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from explanation_module import explain_concept
from learning_path import get_learning_recommendations
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0",
)

app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static",
)

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


# ---------------------------------------------------------
# Request models
# ---------------------------------------------------------

class TextRequest(BaseModel):
    text: str = Field(..., min_length=1)


class QuestionRequest(BaseModel):
    question: str = Field(..., min_length=1)


class TopicRequest(BaseModel):
    topic: str = Field(..., min_length=1)


# ---------------------------------------------------------
# Home page
# ---------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


# ---------------------------------------------------------
# Health check
# ---------------------------------------------------------

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "application": "EduGenie",
        "version": "1.0.0",
    }


# ---------------------------------------------------------
# Q&A
# ---------------------------------------------------------

@app.post("/qa")
async def qa(request: QuestionRequest):
    try:
        answer = answer_question(request.question)

        return {
            "success": True,
            "question": request.question,
            "answer": answer,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Q&A error: {str(exc)}",
        )


# ---------------------------------------------------------
# Explanation
# ---------------------------------------------------------

@app.post("/explain")
async def explain(request: TopicRequest):
    try:
        explanation = explain_concept(request.topic)

        return {
            "success": True,
            "topic": request.topic,
            "explanation": explanation,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Explanation error: {str(exc)}",
        )


# ---------------------------------------------------------
# Quiz
# ---------------------------------------------------------

@app.post("/quiz")
async def quiz(request: TextRequest):
    try:
        quiz = generate_quiz(request.text)

        return {
            "success": True,
            "quiz": quiz,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Quiz generation error: {str(exc)}",
        )


# ---------------------------------------------------------
# Summary
# ---------------------------------------------------------

@app.post("/summarize")
async def summarize(request: TextRequest):
    try:
        summary = summarize_text(request.text)

        return {
            "success": True,
            "summary": summary,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Summary error: {str(exc)}",
        )


# ---------------------------------------------------------
# Learning path
# ---------------------------------------------------------

@app.post("/learn/recommendations")
async def learning_recommendations(request: TopicRequest):
    try:
        recommendations = get_learning_recommendations(
            request.topic
        )

        return {
            "success": True,
            "topic": request.topic,
            "recommendations": recommendations,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Learning path error: {str(exc)}",
        )