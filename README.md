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

## Architecture Notes – Merge Conflict Resolution

The README was modified by two development branches to document different API architecture approaches. The final merged description retains both perspectives.

### Developer-A: REST API Architecture
REST (Representational State Transfer) organizes employee data as resources. Employee operations can use HTTP methods such as GET, POST, PUT and DELETE.

### Developer-B: GraphQL Architecture
GraphQL provides a query-based approach in which clients request the specific employee fields they need through a GraphQL query.

### Final Conflict Resolution
Both REST API and GraphQL architecture descriptions are retained in this README after resolving the merge conflict. These are documented architectural approaches for the Git exercise; they do not imply that both API implementations are deployed in the Flask application.

## Setup Instructions

1. Install Python 3.
2. Install dependencies:

   pip install -r requirements.txt

3. Run the application:

   python app.py

4. Open the application in your browser:

   http://127.0.0.1:5000

## Git Branches
- main – stable project branch
- development – integration branch
- feature/employee-registration – employee registration
- feature/employee-search – employee search
- developer-A – REST API README change
- developer-B – GraphQL README change
