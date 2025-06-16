# server/seed.py

from server.app import app
from server.models import db, Student, Mentor, Cohort
from faker import Faker
import random

faker = Faker()

with app.app_context():
    Student.query.delete()
    Mentor.query.delete()
    Cohort.query.delete()

    print("Seeding mentors...")
    mentors = []
    for _ in range(5):
        first = faker.first_name()
        last = faker.last_name()
        name = f"{first} {last}"
        email = f"{first.lower()}.{last.lower()}@moringaschool.com"
        mentors.append(Mentor(name=name, email=email))
    db.session.add_all(mentors)
    db.session.commit()

    print("Seeding cohorts...")
    cohorts = []
    for _ in range(5):
        cohort_name = f"Cohort-{faker.random_uppercase_letter()}{random.randint(1, 9)}"
        year = random.randint(2020, 2025)
        mentor = random.choice(mentors)
        cohorts.append(Cohort(name=cohort_name, year=year, mentor_id=mentor.id))
    db.session.add_all(cohorts)
    db.session.commit()

    print("Seeding students...")
    students = []
    for _ in range(10):
        first = faker.first_name()
        last = faker.last_name()
        name = f"{first} {last}"
        email = f"{first.lower()}.{last.lower()}@students.moringaschool.com"
        cohort = random.choice(cohorts)
        students.append(Student(name=name, email=email, cohort_id=cohort.id))
    db.session.add_all(students)
    db.session.commit()

    print("Seeding done!")
