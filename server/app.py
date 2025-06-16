from flask import Flask, request, jsonify
from flask_migrate import Migrate

from server import create_app, db
from server.models import Student, Mentor

app = create_app()
migrate = Migrate(app, db)

@app.route('/')
def index():
    return {'message': 'Welcome to Moringa School API'}

# GET students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    students_data = [
        {
            'id': s.id,
            'name': s.name,
            'email': s.email
        }
        for s in students
    ]
    return jsonify(students_data), 200

# GET /mentors 
@app.route('/mentors', methods=['GET'])
def get_mentors():
    mentors = Mentor.query.all()
    mentors_data = [
        {
            'id': m.id,
            'name': m.name,
            'email': m.email
        }
        for m in mentors
    ]
    return jsonify(mentors_data), 200

#  POST /mentors
@app.route('/mentors', methods=['POST'])
def create_mentor():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return {'error': 'Name and email are required'}, 400

    new_mentor = Mentor(name=name, email=email)
    db.session.add(new_mentor)
    db.session.commit()

    return {
        'message': 'Mentor created',
        'mentor': {
            'id': new_mentor.id,
            'name': new_mentor.name,
            'email': new_mentor.email
        }
    }, 201

if __name__ == '__main__':
    app.run(port=5555, debug=True)
