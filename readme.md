# FastAPI Quiz API

This repository contains a simple Quiz API built using FastAPI. The API allows users to retrieve quizzes, submit quiz responses, and fetch quiz results.

## Getting Started

Follow the instructions below to use the FastAPI Quiz API:

### Prerequisites

1. Install [Python](https://www.python.org/downloads/).
2. Install required packages by running:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up a PostgreSQL database and update the `DATABASE_URL` in the `main.py` file with your database credentials.

### Running the FastAPI App

1. Run the FastAPI application:

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

### 2. Submit Quiz Answers

**Endpoint:** `POST /submit`

- Submit quiz answers by sending a JSON payload with the quiz ID, user ID, and user answers.

**Postman Instructions:**
- **Method:** POST
- **URL:** http://127.0.0.1:8000/submit
- **Headers:**
  - `Content-Type: application/json`
- **Body:**
  - **Raw JSON**
    ```json
    {
      "quiz_id": 1,
      "user_id": 1,
      "user_answers": ["B", "C", "A"]
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

## Examples

### Example 1: Retrieve a Quiz

```bash
curl http://127.0.0.1:8000/quizzes/1
