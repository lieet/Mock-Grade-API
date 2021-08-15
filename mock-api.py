from flask import Flask
from flask_restful import Resource, Api
from random import choice, randint, uniform
from math import trunc

app = Flask(__name__)
mock_api = Api(app)

USERS = {
  '1': {'name': 'Aluno #1', 'login': 'aluno1', 'type': 'student'},
  '2': {'name': 'Aluno #2', 'login': 'aluno2', 'type': 'student'},
  '3': {'name': 'Professor #1', 'login': 'professor1', 'type': 'teacher'},
  '4': {'name': 'Professor #2', 'login': 'professor2', 'type': 'teacher'}
}

CLASSES = {
  '1': {'name': 'T01'},
  '2': {'name': 'T02'},
  '3': {'name': 'T03'},
  '4': {'name': 'T04'},
  '5': {'name': 'T05'},
  '6': {'name': 'T06'},
  '7': {'name': 'T07'},
  '8': {'name': 'T08'},
  '9': {'name': 'T09'},
  '10': {'name': 'T10'}
}

def generate_grades(weeks):
  grades = []
  factor = 100
  for i in range(1, weeks):
    pp, pv = trunc(uniform(0,10)*factor)/factor, trunc(uniform(0,10*factor))/factor
    grades.append({'pp': pp, 'pv': pv, 'week': i})
  return grades

class User(Resource):
  def get(self):
    return choice(list(USERS.values()))

class SchoolClass(Resource):
  def get(self):
    return choice(list(CLASSES.values()))

class Grade(Resource):
  def get(self):
    return generate_grades(randint(2,19))

class ClassGrades(Resource):
  def get(self):
    weeks = randint(2,19)
    class_grades = []
    class_grades.append({'name': 'Aluno A', 'grades': generate_grades(weeks)})
    class_grades.append({'name': 'Aluno B', 'grades': generate_grades(weeks)})
    class_grades.append({'name': 'Aluno C', 'grades': generate_grades(weeks)})
    class_grades.append({'name': 'Aluno D', 'grades': generate_grades(weeks)})
    class_grades.append({'name': 'Aluno E', 'grades': generate_grades(weeks)})
    return class_grades

mock_api.add_resource(User, '/user/')
mock_api.add_resource(SchoolClass, '/class/')
mock_api.add_resource(Grade, '/grade/')
mock_api.add_resource(ClassGrades, '/class_grades/')

if __name__ == "__main__":
  app.run(debug=True)