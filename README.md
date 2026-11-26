# Employee Management Portal

A Python Flask-based web application for employee registration, search, and record management.

## Features
- Employee Registration
- Employee Search
- Employee Management

## Technologies
- Python
- Flask
- HTML
- Git and GitHub

## Architecture Details

### REST API Architecture (Developer-A)
REST represents employee data as resources. The application can use HTTP methods such as GET, POST, PUT and DELETE for employee operations.

### GraphQL Architecture (Developer-B)
GraphQL provides a query-based interface where clients request specific employee information through GraphQL queries.

### Conflict Resolution
Both descriptions have been retained after manually resolving the README merge conflict. These are architecture descriptions for the Git workflow exercise.

## Setup Instructions
1. Install Python 3.
2. Install dependencies with: pip install -r requirements.txt
3. Run the application with: python app.py
4. Open http://127.0.0.1:5000 in a browser.

## Git Branches
- main: stable project branch
- development: integration branch
- feature/employee-registration: employee registration
- feature/employee-search: employee search
- developer-A: REST README change
- developer-B: GraphQL README change
