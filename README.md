# Jacaranda

## What I managed to achieve

- Create Flask RESP API that does integer division of 2 numbers.
- Unit testing.
- Dockerizing the application.
- Setting up Sentry and using it as an application monitoring tool.

## What I could have done better

- Setting up Sentry to do error reporting using the organization's media like Slack
- Increase my test coverage.
- Deploy my docker container.

## Prerequisites before you start off the project

### For you to fire up this project locally, you should have the following installed

- [Python 3](https://www.python.org/)
- [Postgres](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)

## How to set up this manually

- `git clone https://github.com/dunnyk/jacaranda.git`
- `cd jacaranda` to navigate to the project folder
- `virtualenv --python=3.10 venv` to create virtual environment
- `source venv/bin/activate` to activate virtual environment
- `pip install -r requirements.txt` to install the dependencies
- `touch .env` to create a new env file
- **copy and paste the sample env and replace with your actual credentials**
- `source .env` to source env variables
- `flask db upgrade` to apply the migration changes
- `python manage.py` to start the server
- Navigate to `http://127.0.0.1:8080` to visit the site

## Sample env

export SQLALCHEMY_DATABASE_URI="postgresql://<your_db_username>:<your_password>@localhost:5432/<your_db_name>"
export SENTRY_DSN="<your_sentry_access>"
**Note: There is no space next to '='**

### docker

- Install Docker: You can download and install Docker for your operating system from the Docker website
- `docker-compose build` to build
- `docker-compose up` to bring up docker

## Project Endpoints

- This is a web app endpoint to the api:
  - Endpoint name `{http://127.0.0.1:8080}/api/divide`

## Running test

- `pytest` To run tests
