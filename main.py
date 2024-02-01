from fastapi import FastAPI, HTTPException, status # Import FastAPI modules for building APIs
from pydantic import BaseModel  # Import Pydantic for data validation
from database import SessionLocal  # Import the SessionLocal object for database sessions
from models import Quiz, UserSubmission  # Import Quiz and UserSubmission models

app = FastAPI() # Create a FastAPI application instance
db = SessionLocal() # Create a global database session instance

class OurBaseModel(BaseModel): # Define a base Pydantic model for common configurations
    class Config:
        from_attributes = True

class QuizResponse(OurBaseModel): # Pydantic model for representing the response of a quiz
    title: str # Title of the quiz
    questions: list[dict] # List of questions in the quiz

class SubmitRequest(OurBaseModel): # Pydantic model for handling submission requests
    quiz_id: int # ID of the quiz being submitted
    user_id: int # ID of the user submitting the quiz
    user_answers: list[str] # List of user's answers to quiz questions

class ResultResponse(OurBaseModel): # Pydantic model for representing the response of a quiz result
    quiz_id: int  # ID of the quiz
    user_id: int  # ID of the user
    user_score: int  # Score achieved by the user
    correct_answers: list[str]  # List of correct answers

# API Endpoint to retrieve quiz information by quiz_id
@app.get("/quizzes/{quiz_id}", response_model=QuizResponse) 
async def get_quiz(quiz_id: int):
    # Open a new database session
    db = SessionLocal()
    # Query the database to find the quiz by quiz_id
    quiz = db.query(Quiz).filter(Quiz.quiz_id == quiz_id).first()
    # Close the database session
    db.close()
    # Check if the quiz was not found
    if not quiz:
        # Raise the status as Quiz not found
        raise HTTPException(status_code=404, detail="Quiz not found")
    return {"title": quiz.title, "questions": quiz.questions} # Return the response with quiz information

# API Endpoint to submit quiz answers and store in the database
@app.post("/submit", response_model=SubmitRequest, status_code=status.HTTP_201_CREATED)
async def submit_quiz(submit_request: SubmitRequest):
    # Open a new database session
    db = SessionLocal()
    # Query the database to find the quiz by quiz_id
    quiz = db.query(Quiz).filter(Quiz.quiz_id == submit_request.quiz_id).first()
    # Check if the quiz was not found
    if not quiz:
        db.close()
        # Raise the status as Quiz not found
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found")
    # Query the database to find the quiz by quiz_id and user by user_id
    find_user=db.query(UserSubmission).filter(UserSubmission.user_id == submit_request.user_id and UserSubmission.quiz_id == submit_request.quiz_id).first()
    # Check if the user has already submitted the quiz
    if find_user is not None:
        # Raise the status as User has already submitted the quiz
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="User has already submitted the quiz")
    # Create a new UserSubmission instance to record user answers as response
    user_submission = UserSubmission(quiz_id=submit_request.quiz_id, user_id=submit_request.user_id, user_answers=submit_request.user_answers)
    #Add the response it to the database
    db.add(user_submission)
    # Commit to the database session
    db.commit()
    # Close the database session
    db.close()
    #return the response of the user
    return submit_request

# API Endpoint to retrieve quiz result by quiz_id and user_id
@app.get("/result/{quiz_id}/{user_id}", response_model=ResultResponse, status_code=status.HTTP_202_ACCEPTED)
async def get_result(quiz_id: int,user_id: int):
    # Open a new database session
    db = SessionLocal()

    # Query the database to find the quiz by quiz_id
    quiz = db.query(Quiz).filter(Quiz.quiz_id == quiz_id).first()
    
    # Check if the quiz was not found
    if not quiz:
        db.close()
        # Raise the status as Quiz not found
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found")

    # Retrieve user answers from the database
    user_submission = db.query(UserSubmission).filter(UserSubmission.quiz_id == quiz_id, UserSubmission.user_id == user_id).first()
    # Close the database session
    db.close()
    # Check if the user submission was not found
    if not user_submission:
        raise HTTPException(status_code=404, detail="User submission not found")
    # Extract user answers and correct answers from the quiz
    user_answers = user_submission.user_answers
    correct_answers = [question["correct_answer"] for question in quiz.questions]
    
    # Calculate the user score by comparing user answers with correct answers
    user_score = sum(answer == correct_answer for answer, correct_answer in zip(user_answers, correct_answers))

    # Return the result response od that user
    return {"quiz_id": quiz_id, "user_id": user_id, "user_score": user_score, "correct_answers": correct_answers}
