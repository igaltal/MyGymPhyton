# /app/services/exercise_service.py
from app import db
from app.models.models import Exercise

def get_exercise_by_code(code_ex):
    return Exercise.query.filter_by(number_exercises=code_ex).first()

def get_all_exercises():
    return Exercise.query.all()

def insert_exercise(name, desc, work, level):
    max_number = db.session.query(db.func.max(Exercise.number_exercises)).scalar() or 0
    new_exercise = Exercise(number_exercises=max_number+1, name_exercises=name, description=desc, work_on=work, level_this=level)
    db.session.add(new_exercise)
    db.session.commit()
