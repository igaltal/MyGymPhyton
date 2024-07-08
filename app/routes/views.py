from app import db
from app.models import Users, City, Gender, Goal, Level, LevelStart, Trainer
from app.services.data_access import get_cities, get_account_by_credentials
from app.services.exercise_service import get_exercise_by_code, get_all_exercises, insert_exercise  
from app.services.user_service import UsersService
from app.utilities.validation_helpers import validate_name, validate_id, check_password, check_phone
from flask import Blueprint, render_template, jsonify, request, redirect, url_for, session, flash

bp = Blueprint('views', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/cities')
def city_list():
    cities = get_cities()
    return jsonify({'cities': [city.name for city in cities]})

@bp.route('/account/<int:user_id>/<user_password>')
def account(user_id, user_password):
    account = get_account_by_credentials(user_id, user_password)
    if account:
        return jsonify({'user_id': account.Id, 'user_password': account.Password})
    return jsonify({'error': 'Account not found'}), 404

@bp.route('/exercises')
def exercises():
    exercises = get_all_exercises()  # Call the function directly
    return jsonify([{'id': exercise.number_exercises, 'name': exercise.name_exercises} for exercise in exercises])

@bp.route('/add_exercise', methods=['POST'])
def add_exercise():
    data = request.json
    result = insert_exercise(data['name'], data['description'], data['work_on'], data['level'])  # Call the function directly
    if result:
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'}), 400

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        id_number = data.get('id_number')
        phone = data.get('phone_prefix') + data.get('phone_number')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        city = data.get('city')
        gender = data.get('gender')
        weight = data.get('weight')
        height = data.get('height')
        level = data.get('level')
        goal = data.get('goal')
        trainer_id = data.get('trainer')
        birthdate = f"{data.get('birthdate_day')}/{data.get('birthdate_month')}/{data.get('birthdate_year')}"

        # Server-side validation
        if not validate_name(first_name) or not validate_name(last_name):
            flash('Invalid name')
            return render_template('register.html')

        if not validate_id(id_number):
            flash('Invalid ID')
            return render_template('register.html')

        if UsersService.check_id(id_number):
            flash('User ID already exists')
            return render_template('register.html')

        if UsersService.check_phone(phone):
            flash('Phone number already exists')
            return render_template('register.html')
        
        if not check_password(password, confirm_password):
            flash('Passwords do not match')
            return render_template('register.html')

        user_data = {
            'id': id_number,
            'name': first_name,
            'last_name': last_name,
            'phone': phone,
            'num_city': city,
            'this_date': birthdate,
            'password': password,
            'date_b': birthdate,
            'gender': gender,
            'weight': weight,
            'height': height,
            'level_start': level,
            'goal': goal,
            'trainer': trainer_id,
            'rank': 0,  # assuming a default value
            'itkadmot': 0  # assuming a default value
        }

        try:
            UsersService.insert_person(user_data)
            flash('Registration successful')
            return redirect(url_for('views.home'))
        except Exception as e:
            flash(str(e))
            return render_template('register.html')

    cities = City.query.all()
    genders = Gender.query.all()
    levels = Level.query.all()
    level_starts = LevelStart.query.all()
    goals = Goal.query.all()
    trainers = Trainer.query.all()

    return render_template('register.html', cities=cities, genders=genders, levels=levels, level_starts=level_starts, goals=goals, trainers=trainers)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        
        if not user_id or not password:
            flash('ID and password are required')
            return render_template('login.html')

        user = UsersService.check_id(user_id)
        if not user:
            flash('User ID does not exist')
            return render_template('login.html')

        if user.Password == password:
            session['Id'] = user.Id
            session['Name'] = user.Name
            flash('You were successfully logged in')
            return redirect(url_for('views.home'))
        else:
            flash('Invalid password')
            return render_template('login.html')
    
    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('views.home'))

@bp.route('/users')
def users():
    users = UsersService.get_all()
    return render_template('users.html', users=users)

@bp.route('/validate_name', methods=['POST'])
def validate_name_route():
    name = request.json.get('name', '')
    if validate_name(name):
        return jsonify({'valid': True})
    return jsonify({'valid': False, 'message': 'Invalid name. Names should be alphabetic and longer than 2 characters.'})

@bp.route('/validate_id', methods=['POST'])
def validate_id_route():
    id_number = request.json.get('id_number', '')
    if validate_id(id_number):
        return jsonify({'valid': True})
    return jsonify({'valid': False, 'message': 'Invalid ID.'})

@bp.route('/validate_phone', methods=['POST'])
def validate_phone_route():
    phone = request.json.get('phone', '')
    if check_phone(phone):
        return jsonify({'valid': True})
    return jsonify({'valid': False, 'message': 'Invalid phone number.'})

@bp.route('/validate_password', methods=['POST'])
def validate_password_route():
    password = request.json.get('password', '')
    confirm_password = request.json.get('confirm_password', '')
    if check_password(password, confirm_password):
        return jsonify({'valid': True})
    return jsonify({'valid': False, 'message': 'Passwords do not match.'})

@bp.route('/user_dashboard')
def user_dashboard():
    if 'Id' not in session:
        flash('You need to log in to access the dashboard')
        return redirect(url_for('views.login'))
    
    user_id = session['Id']
    user_details = UsersService.get_user_details(user_id)
    return render_template('user_dashboard.html', user=user_details)
