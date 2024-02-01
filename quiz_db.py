from database import SessionLocal # Import the SessionLocal object from the database module
import models  # Import the models module containing database models

# Sample data for quizzes in JSON format
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

# Function to feed quiz data into the database
def feed_quizzes_to_db():
    # Create a database session using the SessionLocal object
    db = SessionLocal()
    # Iterate through each quiz data and add it to the database
    for quiz_data in quizzes_data:
        # Create a Quiz database model instance with the quiz data
        db_quiz = models.Quiz(**quiz_data)
        # Add the quiz to the session
        db.add(db_quiz)
    # Commit the changes to the database
    db.commit()
    # Close the session
    db.close()

# Create database tables and feed quizzes data into the database
models.create_tables()
feed_quizzes_to_db()