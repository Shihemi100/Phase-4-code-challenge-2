# Late Night Show API

A RESTful Flask API backend for managing late night show episodes, guests, and their appearances with ratings. Includes user authentication with JWT.

## Features

- User registration and login with JWT authentication  
- CRUD operations for Episodes, Guests, Appearances  
- Validation for appearance ratings (1 to 5)  
- Relationships between guests, episodes, and appearances  
- Secure password hashing  

## Technologies Used

- Python 3.x  
- Flask  
- Flask-SQLAlchemy  
- Flask-Migrate  
- Flask-JWT-Extended  
- PostgreSQL (or any SQL database supported by SQLAlchemy)  
- Werkzeug Security for password hashing  

## Installation

1. Clone the repository  
   ```bash
   git clone git@github.com:Kiago-prog/python-p4-iam-putting-it-all-together-lab.git
   cd late-night-show-api
```

2. Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```


3. Install dependencies

```bash
pip install -r requirements.txt
```


4. Configure environment variables

Create a `.env` file in the root directory and add the following:


5. Run database migrations

Initialize and apply migrations to create the database schema:

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

6. Run the application

Start the Flask development server:

```bash
flask run
```


# API Endpoints
## Authentication
POST /register — Register a new user

POST /login — Login and get JWT token

## Episodes
GET /episodes — List all episodes

GET /episodes/<id> — Get episode details including appearances

DELETE /episodes/<id> — Delete an episode (protected route)

Guests
GET /guests — List all guests

Appearances
POST /appearances — Create an appearance with rating (protected route)

Usage Notes
Use the JWT access token from /login in the Authorization header as:
Authorization: Bearer <access_token>

Appearance ratings must be integers between 1 and 5.

License
MIT License