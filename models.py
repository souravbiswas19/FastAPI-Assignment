from sqlalchemy import Column, Integer, String, JSON
from database import engine, Base

# Database Models
class Quiz(Base): #Represents a Quiz in the database.
    # Attributes:
    __tablename__ = "quizzes"
    quiz_id = Column(Integer, primary_key=True, index=True) # quiz_id (int): A unique identifier for each quiz.
    title = Column(String, index=True) # title (str): The title or name of the quiz.
    questions = Column(JSON) # questions (JSON): A JSON field to store quiz questions and options.

class UserSubmission(Base): #Represents a User Submission in the database.
    __tablename__ = "user_submissions" #tablename of the User Submission
    #Attributes:
    quiz_id = Column(Integer) #quiz_id (int): A reference to the quiz the user submitted.
    user_id = Column(Integer, primary_key=True, index=True) #user_id (int): A unique identifier for each user submission.
    user_answers = Column(JSON) #user_answers (JSON): A JSON field to store user-submitted answers.

def create_tables(): # Function to create the necessary database tables - 'quizzes' and 'user_submissions'
    Base.metadata.create_all(bind=engine) #This function utilizes SQLAlchemy to create the tables defined in the models.