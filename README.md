# Job Portal
## Description
Job Portal is a Django-based web application designed to connect employers with job seekers in a simple and organized way.
Employers can create an account, post job openings with details such as job title, company, location, salary, and description, and manage their listings from a personal dashboard.
Job seekers can browse available jobs, search for jobs by title, and apply directly by submitting a cover letter along with their resume.
The platform uses role-based access control to ensure that employers and job seekers have access only to the features relevant to their roles, creating a clean, secure, and user-friendly experience.
## Features
### User Management
- User registration and authentication
- Two user roles: **Employer** and **Seeker**
- Role-based access control
### Employer Features
- Create and manage job listings
- Post jobs with title, company, location, salary, and description
- Edit and delete posted jobs
- "My Jobs" dashboard
- View applicant counts for posted jobs
### Job Seeker Features
- Browse all available jobs
- Search jobs by title
- Apply for jobs
- Submit a cover letter and resume
- "My Applications" dashboard
- Track submitted job applications
### Administration
- Django admin panel
- Manage users
- Manage job listings
- Manage job applications
## Technologies Used
- Python
- Django
- HTML
- CSS
- SQLite
## Project Requirements
The required Python packages and dependencies are listed in the `requirements.txt` file.
## Installation
1. Clone the repository

git clone https://github.com/tayyabadev11/job-portal.git

cd job-portal

2. Create and activate a virtual environment

python -m venv venv

venv\Scripts\activate

3. Install the required packages

pip install -r requirements.txt

4. Create a `.env` file in the project root and add

SECRET_KEY=your-secret-key

DEBUG=True

DB_NAME=db.sqlite3

5. Run migrations

python manage.py makemigrations

python manage.py migrate

6. Create a superuser (optional, for admin access)

python manage.py createsuperuser

7. Run the development server

python manage.py runserver

8.Open `http://127.0.0.1:8000/` in your browser

## Environment
Project configuration and sensitive settings are managed using environment variables.
## Author
Tayyaba


