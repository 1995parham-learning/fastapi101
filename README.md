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

First, devise the API to accommodate the following operations:

```
GET /students
Retrieve a list of created students

POST /students
Create a student

DELETE /students/:id
Remove a student identified by the given ID

GET /students/:id
Fetch the details of a student identified by the given ID
```

For student identification, any unique string can be used. The provided Student model serves as a reference,
though alternative models can be utilized for requests and responses.

```python
from datetime import date
from pydantic import BaseModel

class Student(BaseModel):
    id: str  # Unique identification manually generated
    first_name: str  # First name provided by the user
    last_name: str  # Last name provided by the user
    registration_date: date  # Date of registration
    graduation_date: date | None = None  # Graduation date (if applicable)
    average: float  # Average score provided by the user
```

Implement the design using [FastAPI](https://fastapi.tiangolo.com/) with asynchronous handlers.
Utilize [`pipenv`](https://pipenv.pypa.io/en/latest/) or [`poetry`](https://python-poetry.org/) for project setup,
and ensure inclusion of a README detailing how to run the project.

> [!NOTE]
> Database usage is unnecessary for now; data can be stored in memory.

> [!NOTE]
> Utilize [`pydantic`](https://docs.pydantic.dev/latest/) for requests, responses, and models due to its excellent integration with FastAPI.

To gain a better understanding of asynchronous programming, include sleep in handlers.

```python
import asyncio

await asyncio.sleep(10)
```

```python
import time

time.sleep(10)
```

Invoke your APIs multiple times with `async` and `sync` sleep, recording response times to observe differences.

Ensure a clean design with separation of logic and views using [Dependency Injection](https://fastapi.tiangolo.com/tutorial/dependencies/).

Write tests for the API based on [FastAPI documentation](https://fastapi.tiangolo.com/tutorial/testing/), and leverage GitHub Actions for testing and linting.

> [!CAUTION]
> The `uvicorn` can have multiple workers, test and see your in-memory storage works with them or not?
> Is there any solution in your mind?

Now you know the issue, so provide the database and use the in-memory store only in tests.
For using database, you can use [`sqlmodel`](https://github.com/tiangolo/sqlmodel) which is the FastAPI friend.
After switching to the database, you can update tests based on [manual](https://fastapi.tiangolo.com/advanced/testing-database/).

When you have the backend API, you need to have a way to communicate the API with your frontend team.
I can suggest two solutions here, [Postman](https://www.postman.com/) and [Swagger](https://swagger.io/) but which one prefered by you?

If you want to write this project with your partner, how did you do that?

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
