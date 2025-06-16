from server import db
from sqlalchemy_serializer import SerializerMixin

class Student(db.Model, SerializerMixin):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    cohort_id = db.Column(db.Integer, db.ForeignKey('cohorts.id'))
    cohort = db.relationship('Cohort', back_populates='students')


class Mentor(db.Model, SerializerMixin):
    __tablename__ = 'mentors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    cohorts = db.relationship('Cohort', back_populates='mentor', cascade='all, delete-orphan')


class Cohort(db.Model, SerializerMixin):
    __tablename__ = 'cohorts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    mentor_id = db.Column(db.Integer, db.ForeignKey('mentors.id'), nullable=False)
    mentor = db.relationship('Mentor', back_populates='cohorts')
    students = db.relationship('Student', back_populates='cohort', cascade='all, delete-orphan')
