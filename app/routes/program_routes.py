# /app/routes/program_routes.py
from flask import Blueprint, request, jsonify
from app.services import program_service

bp = Blueprint('program', __name__)

@bp.route('/program/<int:coaching_id>')
def get_program(coaching_id):
    exercises = program_service.get_program_exercises(coaching_id)
    return jsonify([{'name': ex.name, 'num_back': ex.num_back, 'retu_number': ex.retu_number, 'work_on': ex.work_on} for ex in exercises])

@bp.route('/program/add', methods=['POST'])
def add_exercise():
    data = request.json
    program_service.insert_exercise_into_program(
        data['coaching_id'], data['exercise_id'], data['retu2'], data['retu'], data['work_on']
    )
    return jsonify({'status': 'success'})


