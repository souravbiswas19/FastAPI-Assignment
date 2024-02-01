# FastAPI Quiz API

This repository contains a simple Quiz API built using FastAPI. The API allows users to retrieve quizzes, submit quiz responses, and fetch quiz results.

## Follow the instructions below to use the FastAPI Quiz API:

### Prerequisites

1. Install required packages by running:
    
    ```bash
    pip install fastapi[all] sqlalchemy psycopg2 psycopg2-binary uvicorn[standard]

    ```

2. Set up a PostgreSQL database and update the database url in the `database.py` file with your database credentials.

### Running the FastAPI App

1. Run the FastAPI application:

    Step 1 - Run the `quiz_db.py` file using code runner or in the terminal 

    ```bash
    python quiz_db.py
    ```

    This will create the `quizzes` and `user_submissions` tables 'ONCE' in the Postgresql Database with database name 'Quiz. This file will also insert the 3 predefined set of quizzes with 3 quizzes in each set with 4 options in the database.
    
    Step 2 - Run Uvicorn in `--reload` mode

    ```bash
    uvicorn main:app --reload
    ```


2. The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### 1. Retrieve a Specific Quiz

**Endpoint:** `GET /quizzes/{quiz_id}`

- Retrieve a specific quiz by providing the `{quiz_id}` parameter.

**Postman Instructions:**
- **Method:** GET
- **URL:** http://127.0.0.1:8000/quizzes/{quiz_id}
  - Replace `{quiz_id}` with the ID of the quiz you want to retrieve.
  - Eg: http://127.0.0.1:8000/quizzes/1

### 2. Submit Quiz Answers

**Endpoint:** `POST /submit`

- Submit quiz answers by sending a JSON payload with the quiz ID, user ID, and user answers.

**Postman Instructions:**
- **Method:** POST
- **URL:** http://127.0.0.1:8000/submit
- **Body:**
  - **JSON**
    ```json
    {
      "quiz_id": 1,
      "user_id": 1,
      "user_answers": ["B", "A", "A"]
    }
    ```

### 3. Get Quiz Result

**Endpoint:** `GET /result/{quiz_id}/{user_id}`

- Get the quiz result for a specific quiz and user by providing `{quiz_id}` and `{user_id}` parameters.

**Postman Instructions:**
- **Method:** GET
- **URL:** http://127.0.0.1:8000/result/{quiz_id}/{user_id}
  - Replace `{quiz_id}` with the ID of the quiz.
  - Replace `{user_id}` with the ID of the user.
  - Eg: http://127.0.0.1:8000/result/1/1 for quiz_id: 1 and user_id: 1 respectively
