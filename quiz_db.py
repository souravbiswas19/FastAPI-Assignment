from database import SessionLocal
import models
quizzes_data = [
    {
        "title": "Python Basics Quiz",
        "questions": 
        [
            {
                "statement": "What is the result of print(5 + 3)?",
                "options": ["A. 7", "B. 8", "C. 9", "D. 10"],
                "correct_answer": "B"
            },
            {
                "statement": "Which keyword is used for defining a function in Python?",
                "options": ["A. def", "B. function", "C. define", "D. fun"],
                "correct_answer": "A"
            },
            {
                "statement": "What is the output of print('Hello' + ' World')?",
                "options": ["A. Hello World", "B. HelloWorld", "C. Hello + World", "D. Error"],
                "correct_answer": "A"
            }
        ]
    },
    {
        "title": "Python Data Structures Quiz",
        "questions": 
        [
            {
                "statement": "Which data structure uses the Last In, First Out (LIFO) principle?",
                "options": ["A. Stack", "B. Queue", "C. Linked List", "D. Array"],
                "correct_answer": "A"
            },
            {
                "statement": "What is the main purpose of a dictionary in Python?",
                "options": ["A. Sorting elements", "B. Storing key-value pairs", "C. Sequential access of elements", "D. Storing integers only"],
                "correct_answer": "B"
            },
            {
                "statement": "Which method is used to add an element at the end of a list?",
                "options": ["A. append()", "B. insert()", "C. extend()", "D. add()"],
                "correct_answer": "A"
            }
        ]
    },
    {
        "title": "Python OOP Quiz",
        "questions": 
        [
            {
                "statement": "What is the concept of bundling data and methods that operate on the data?",
                "options": ["A. Inheritance", "B. Polymorphism", "C. Abstraction", "D. Encapsulation"],
                "correct_answer": "D"
            },
            {
                "statement": "In Python, which keyword is used to create a class?",
                "options": ["A. class", "B. create", "C. define", "D. struct"],
                "correct_answer": "A"
            },
            {
                "statement": "What is the purpose of the __init__ method in a Python class?",
                "options": ["A. Initializing class attributes", "B. Deleting the class", "C. Defining class methods", "D. Importing external modules"],
                "correct_answer": "A"
            }
        ]
    }
]

def feed_quizzes_to_db():
    db = SessionLocal()
    for quiz_data in quizzes_data:
        db_quiz = models.Quiz(**quiz_data)
        db.add(db_quiz)
    db.commit()
    db.close()

    
models.create_tables()
feed_quizzes_to_db()