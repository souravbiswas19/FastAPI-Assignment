from sqlalchemy import create_engine, Column, Integer, String, JSON

from database import Base, engine

def create_tables():
    Base.metadata.create_all(bind=engine)

class Quiz(Base):
    __tablename__ = "quiz"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    questions = Column(JSON)