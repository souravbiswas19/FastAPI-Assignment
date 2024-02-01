from sqlalchemy import Column, Integer, String, JSON
from database import engine, Base

# Database Models
class Quiz(Base):
    __tablename__ = "quizzes"
    quiz_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    questions = Column(JSON)

class UserSubmission(Base):
    __tablename__ = "user_submissions"
    quiz_id = Column(Integer)
    user_id = Column(Integer, primary_key=True, index=True)
    user_answers = Column(JSON)

def create_tables():
    Base.metadata.create_all(bind=engine)