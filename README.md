
# CodeAlpha Data Redundancy Removal System

## Project Overview
The Data Redundancy Removal System is a Python-based web
application that validates incoming records and prevents duplicate
email addresses from being stored in an SQLite database.

## Objectives
- Validate user input.
- Detect duplicate email addresses.
- Prevent duplicate records.
- Store records in an SQLite database.
- Display saved records through a web interface.

## Technologies Used
- Python
- Flask
- SQLite
- HTML
- CSS
- GitHub

## Features
- Simple web-based form.
- Name and email validation.
- Case-insensitive email duplicate detection.
- SQLite database storage.
- Display of saved records.
- Success and error messages.

## Project Structure
- app.py: Main Flask application.
- templates/index.html: Web interface.
- requirements.txt: Python dependencies.
- .gitignore: Excludes local files and the virtual environment.

## Requirements
- Python 3.10 or newer.
- pip.

## How to Run

1. Clone the repository:
   git clone YOUR_GITHUB_REPOSITORY_URL

2. Open the project directory:
   cd CodeAlpha_DataRedundancyRemovalSystem

3. Create a virtual environment:
   python -m venv .venv

4. Activate it on Windows:
   .venv\Scripts\Activate.ps1

5. Install dependencies:
   python -m pip install -r requirements.txt

6. Start the application:
   python app.py

7. Open the application in your browser:
   http://127.0.0.1:5000

## Testing
1. Submit a new name and email.
2. Verify that the record is saved.
3. Submit the same email again.
4. Verify that the duplicate is rejected.
5. Check that saved records appear in the table.

## Database Integrity
The email column has a UNIQUE constraint in SQLite.
Email addresses are converted to lowercase before insertion.

## Limitations
This project is a local prototype. It is not yet deployed
to a cloud hosting platform.

## Future Improvements
- Cloud deployment.
- Automated testing.
- Authentication and authorization.
- Enhanced data validation.

## Internship
CodeAlpha Cloud Computing Internship - Task 1
