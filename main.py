from fastapi import FastAPI, HTTPException, Query, Path
from pydantic import BaseModel
from database import SessionLocal
import models

app = FastAPI()

class QuizResponse(BaseModel):
    quiz_id: int
    title: str
    questions: list[dict]

class SubmitRequest(BaseModel):
    quiz_id: int
    user_answers: list[str]

class ResultResponse(BaseModel):
    quiz_id: int
    user_score: int
    correct_answers: list[str]

# Example quizzes data
quizzes_data = [
    {"title": "Math Quiz", "questions": [
        {"statement": "What is 2 + 2?", "options": ["A. 3", "B. 4", "C. 5", "D. 6"], "correct_answer": "B"},
        {"statement": "What is 3 * 5?", "options": ["A. 8", "B. 12", "C. 15", "D. 18"], "correct_answer": "C"},
        {"statement": "What is 10 / 2?", "options": ["A. 2", "B. 4", "C. 5", "D. 8"], "correct_answer": "B"}
    ]},
    {"title": "Science Quiz", "questions": [
        {"statement": "What is the capital of France?", "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"], "correct_answer": "A"},
        {"statement": "What is the largest planet in our solar system?", "options": ["A. Mars", "B. Jupiter", "C. Saturn", "D. Venus"], "correct_answer": "B"},
        {"statement": "What gas do plants absorb from the atmosphere?", "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"], "correct_answer": "C"}
    ]}
]

# Seed the quizzes data into the database
def seed_quizzes():
    db = SessionLocal()
    for quiz_data in quizzes_data:
        db_quiz = models.Quiz(**quiz_data)
        db.add(db_quiz)
    db.commit()
    db.close()

seed_quizzes()


@app.get("/quizzes/{quiz_id}", response_model=QuizResponse)
async def get_quiz(quiz_id: int = Path(..., title="The ID of the quiz to retrieve")):
    db = SessionLocal()
    quiz = db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()
    db.close()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return {"title": quiz.title, "questions": quiz.questions}

@app.post("/submit", response_model=ResultResponse)
async def submit_quiz(submit_request: SubmitRequest):
    db = SessionLocal()
    quiz = db.query(models.Quiz).filter(models.Quiz.id == submit_request.quiz_id).first()
    db.close()

    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")

    user_answers = submit_request.user_answers
    correct_answers = [question["correct_answer"] for question in quiz.questions]
    user_score = sum(answer == correct_answer for answer, correct_answer in zip(user_answers, correct_answers))

    return {"quiz_id": submit_request.quiz_id, "user_score": user_score, "correct_answers": correct_answers}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
