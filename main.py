from fastapi import FastAPI, HTTPException, Path, status
from pydantic import BaseModel
from database import SessionLocal
from models import Quiz, UserSubmission

app = FastAPI()
db = SessionLocal()

class OurBaseModel(BaseModel):
    class Config:
        from_attributes = True

class QuizResponse(OurBaseModel):
    title: str
    questions: list[dict]

class SubmitRequest(OurBaseModel):
    quiz_id: int
    user_id: int
    user_answers: list[str]

class ResultResponse(OurBaseModel):
    quiz_id: int
    user_id: int
    user_score: int
    correct_answers: list[str]

@app.get("/quizzes/{quiz_id}", response_model=QuizResponse)
async def get_quiz(quiz_id: int):
    db = SessionLocal()
    quiz = db.query(Quiz).filter(Quiz.quiz_id == quiz_id).first()
    db.close()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return {"title": quiz.title, "questions": quiz.questions}

@app.post("/submit", response_model=SubmitRequest, status_code=status.HTTP_201_CREATED)
async def submit_quiz(submit_request: SubmitRequest):
    db = SessionLocal()
    quiz = db.query(Quiz).filter(Quiz.quiz_id == submit_request.quiz_id).first()
    if not quiz:
        db.close()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found")
    
    find_user=db.query(UserSubmission).filter(UserSubmission.user_id == submit_request.user_id and UserSubmission.quiz_id == submit_request.quiz_id).first()
    if find_user is not None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="User has already submitted the quiz")

    user_submission = UserSubmission(quiz_id=submit_request.quiz_id, user_id=submit_request.user_id, user_answers=submit_request.user_answers)
    db.add(user_submission)
    db.commit()

    db.close()
    return submit_request

@app.get("/result/{quiz_id}/{user_id}", response_model=ResultResponse, status_code=status.HTTP_202_ACCEPTED)
async def get_result(quiz_id: int,user_id: int):
    db = SessionLocal()
    quiz = db.query(Quiz).filter(Quiz.quiz_id == quiz_id).first()

    if not quiz:
        db.close()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found")

    # Retrieve user answers from the database
    user_submission = db.query(UserSubmission).filter(UserSubmission.quiz_id == quiz_id, UserSubmission.user_id == user_id).first()
    db.close()

    if not user_submission:
        raise HTTPException(status_code=404, detail="User submission not found")

    user_answers = user_submission.user_answers
    correct_answers = [question["correct_answer"] for question in quiz.questions]
    user_score = sum(answer == correct_answer for answer, correct_answer in zip(user_answers, correct_answers))

    return {"quiz_id": quiz_id, "user_id": user_id, "user_score": user_score, "correct_answers": correct_answers}
