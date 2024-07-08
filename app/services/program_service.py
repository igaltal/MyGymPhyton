# /app/services/program_service.py
from app import db
from app.models.models import CoachingProgram, Exercise, ProgramExercise
from app.models import Users


def get_program_exercises(coaching_id):
    return db.session.query(
        Exercise.name, ProgramExercise.num_back, ProgramExercise.retu_number, ProgramExercise.work_on
    ).join(ProgramExercise, Exercise.id == ProgramExercise.exercise_id
           ).filter(ProgramExercise.coaching_id == coaching_id).all()

def insert_exercise_into_program(coaching_id, exercise_id, retu2, retu, work_on):
    new_program_exercise = ProgramExercise(
        coaching_id=coaching_id, exercise_id=exercise_id,
        retu_number=retu2, num_back=retu, work_on=work_on
    )
    db.session.add(new_program_exercise)
    db.session.commit()

def update_program_exercise(coaching_id, exercise_id, retu2, retu):
    program_exercise = ProgramExercise.query.filter_by(
        coaching_id=coaching_id, exercise_id=exercise_id).first()
    if program_exercise:
        program_exercise.retu_number = retu2
        program_exercise.num_back = retu
        db.session.commit()

def delete_exercise_from_program(coaching_id, exercise_id):
    ProgramExercise.query.filter_by(
        coaching_id=coaching_id, exercise_id=exercise_id).delete()
    db.session.commit()

def get_all_exercises_in_program(coaching_id):
    return ProgramExercise.query.filter_by(coaching_id=coaching_id).all()
