#app/routes/user_routes.py
from flask import Blueprint, request, jsonify
from app.models import Users
from app import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    if not data.get('name') or not data.get('id'):  # Simplified validation example
        return jsonify({'error': 'Invalid data'}), 400

    new_user = Users(
        name=data['name'],
        last_name=data['last_name'],
        phone=data['phone'],
        num_city=data['num_city'],
        this_date=data['this_date'],
        password=data['password'],
        date_b=data['date_b'],
        gender=data['gender'],
        weight=data['weight'],
        height=data['height'],
        level_start=data['level_start'],
        goal=data['goal'],
        trainer=data['trainer'],
        rank=data['rank'],
        itkadmot=data['itkadmot']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'status': 'User added'}), 201
