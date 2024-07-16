# Welcome to the Technical Interview

## Project Overview

You will be working on a small Django project to demonstrate your proficiency in using Celery for distributed task scheduling, writing comprehensive unit tests, and using Docker and Docker-Compose. You have 60 minutes to complete the following tasks.

Project Repo: https://github.com/Extended-ERP/interview-app.git

## Instructions

1. **Celery Task (20 minutes)**
    - Implement a Celery task that adds two numbers.
    - Schedule the task to run once using Celery Beat.
    - Ensure the task is correctly configured and executed.
    - Demonstrate the task execution by logging output, creating a database entry, or showing results in Django admin.

2. **Unit Tests (20 minutes)**
    - Write unit tests for the provided Django model (`Item`).
    - Ensure the tests cover the model methods and any edge cases.

3. **Docker and Docker-Compose (20 minutes)**
    - Write a `docker-compose.yml` file to set up the Django app and a PostgreSQL database.
    - Ensure the services are correctly configured and can communicate with each other.

## Setup Instructions

1. **Clone the Repository**
    ```bash
    git clone https://github.com/Extended-ERP/interview-app.git
    cd interview_app
    ```

2. **Setup Virtual Environment and Install Dependencies**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Run Initial Migrations**
    ```bash
    python manage.py migrate
    ```

4. **Create a Superuser for Django Admin**
    ```bash
    python manage.py createsuperuser
    ```

5. **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

6. **Build and Run Docker Containers**
    ```bash
    docker-compose up --build
    ```

## Demonstrating Task Execution

- **Log Output**: Check the logs in the Celery worker terminal to see the task result.
- **Database Entry**: Query the `TaskResult` model to verify the task result is saved in the database.
- **Django Admin**: Log in to the Django admin interface at `/admin/` to view the task results under the `TaskResult` model.

## Submission

Submit your final code by creating a Pull Request (PR) to the GitHub repository.

If you have any questions during the interview, feel free to ask your interviewer for clarification.
