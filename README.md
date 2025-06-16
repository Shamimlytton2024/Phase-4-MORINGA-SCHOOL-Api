# MORINGA-SCHOOL API

This is a RESTful API for managing students, mentors, and cohorts in a fictional school environment. It is built using Flask, SQLAlchemy, and SQLite, and includes routes to fetch and add data related to mentors and students.

## Project Structure

MORINGA-SCHOOL/
├── server/
│   ├── app.py            # Main Flask application and routes
│   ├── models.py         # SQLAlchemy models (Student, Mentor, Cohort)
│   ├── config.py         # App factory and database config
│   ├── seed.py           # Database seeding script
│   ├── __init__.py       # Required for Python module
├── migrations/           # Auto-generated database migrations
├── instance/             # SQLite database file gets created here
├── moringa.db            # SQLite database file
├── README.md             # You're here!
├── requirements.txt      # Python dependencies


### How to Run the Project

1.  Install Dependencies

Make sure you're in a virtual environment:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

2.  Set Up the Database

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

3.  Seed the Database

python3 server/seed.py


4.  Run the Server

python3 server/app.py

Server runs on: http://localhost:5555


 #### API Endpoints

* GET /students

Returns a list of all students.

 * GET /mentors

Returns a list of all mentors.

* POST /mentors

Create a new mentor.
Request Body:
'''json
{
  "name": "Jerry Sirima",
  "email": "jerry.sirima@moringaschool.com"
}



  #### Tech Stack

    Python 3

    Flask

    Flask-SQLAlchemy

    Flask-Migrate

    SQLite

    Faker (for seed data)

 ## Contributors

    [Shamim kalande] (Melon Obade, Brian Mongare, Dedan Opiyo,Eslie, Joan Kori)


# License

This project is licensed under the MIT License.









