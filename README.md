<h1 align="center">FastAPI 101</h1>

<p align="center">
    <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/1995parham-learning/fastapi101/ci.yml?logo=github&style=for-the-badge">
    <img alt="Codecov" src="https://img.shields.io/codecov/c/github/1995parham-learning/fastapi101?logo=codecov&style=for-the-badge">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/1995parham-learning/fastapi101?logo=github&style=for-the-badge">
</p>

## Introduction

[FastAPI](https://fastapi.tiangolo.com/) is a python framework to have HTTP server with lots of typing,
during the project I will try to set up database and also commands for doing common commands.

## Description

First design the API for following operations:

```
GET /students
List the created students

POST /students
Create an student

DELETE /students/:id
Delete students with the given identification

GET /students/:id
Retrieve the student with the given identification
```

Feel free to use any unique string as an identification for students. The following model
should be your model for student, but you can use different models for your request and response.

```python
class Student:
  # unique identification manually generated
  id: str
  # first name given by the user
  first_name: str
  # last name given by the user
  last_name: str
  # the date in which the creation api is called
  registration_date: datetime.date
  # graduation date given by user
  graduation_date: datetime.date | None
  # average score given by user
  average: float
```

Implement the design using [FastAPI](https://fastapi.tiangolo.com/) (make sure you are using `async` handlers),
set up the project using [`pipenv`](https://pipenv.pypa.io/en/latest/) or [`poerty`](https://python-poetry.org/),
and make sure you have a README for how to run the project.

> [!NOTE]
> There is no need to use database for now, and you can store data into memory.

> [!NOTE]
> Use [`pydantic`](https://docs.pydantic.dev/latest/) for request, response and models.
> They have very good integration with FastAPI and its friends.

To understand asynchronous programming better, add sleep into your handlers as follows:

```python
import asyncio

await asyncio.sleep(10)
```

```python
import time

time.sleep(10)
```

Call your APIs in both cases multiple times and write down the response times.
Can you summarize what happened? And what is the difference?

Make sure your design is clean and have multiple modules (you can use current repository to have an idea about the structure).
Use [Dependency Injection](https://fastapi.tiangolo.com/tutorial/dependencies/) to separate logic from your views.

Write tests for your API based on the [FastAPI documentation](https://fastapi.tiangolo.com/tutorial/testing/).

> [!NOTE]
> GitHub Actions is your friend, use them to test and lint your project.

> [!CAUTION]
> The `uvicorn` can have multiple workers, test and see your in-memory storage works with them or not?

## How to run?

You can run server using `uvicorn` directly,

```bash
uvicorn app.main:app --reload
```

or you can run it using the CLI

```bash
python main.py
```

## How to `curl`

You can create a user with

```bash
curl 127.0.0.1:1378/users/ -H 'Content-Type: application/json' -d '{ "first_name": "Parham", "last_name": "Alvani", "average": 19.0  }'
```

and then list the created users with

```bash
curl 127.0.0.1:1378/users/
```
