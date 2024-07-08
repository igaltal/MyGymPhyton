from sqlalchemy.exc import SQLAlchemyError
from app import db
from app.models import Users, City, Gender, Goal, Level, LevelStart, Trainer

class UsersService:
    @staticmethod
    def insert_person(user_data):
        try:
            new_user = Users(
                Id=user_data['id'],
                Name=user_data['name'],
                LastName=user_data['last_name'],
                Pelepone=user_data['phone'],
                NumCity=user_data['num_city'],
                Thisdata=user_data['this_date'],
                Password=user_data['password'],
                Date=user_data['date_b'],
                Gender=user_data['gender'],
                Weight=user_data['weight'],
                Height=user_data['height'],
                LevelStart=user_data['level_start'],
                Goal=user_data['goal'],
                Trainer=user_data['trainer'],
                Rank=user_data['rank'],
                Itkadmot=user_data['itkadmot']
            )
            db.session.add(new_user)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Database error: {str(e)}")

    @staticmethod
    def check_id(user_id):
        try:
            return Users.query.filter_by(Id=user_id).first()
        except SQLAlchemyError as e:
            raise Exception(f"Database error: {str(e)}")

    @staticmethod
    def check_phone(phone):
        try:
            return Users.query.filter_by(Pelepone=phone).first()
        except SQLAlchemyError as e:
            raise Exception(f"Database error: {str(e)}")

    @staticmethod
    def check_password(password, id):
        try:
            user = Users.query.filter_by(Id=id, Password=password).first()
            return user is not None
        except SQLAlchemyError as e:
            raise Exception(f"Database error: {str(e)}")

    @staticmethod
    def get_user_name(id):
        try:
            user = Users.query.filter_by(Id=id).first()
            return user.Name if user else None
        except SQLAlchemyError as e:
            raise Exception(f"Database error: {str(e)}")

    @staticmethod
    def update_user_profile(id, updates):
        try:
            user = Users.query.filter_by(Id=id).first()
            if user:
                for key, value in updates.items():
                    setattr(user, key, value)
                db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Database error: {str(e)}")

    @staticmethod
    def get_all():
        try:
            return Users.query.all()
        except SQLAlchemyError as e:
            raise Exception(f"Database error: {str(e)}")

    @staticmethod
    def insert_user(form_data):
        user = Users(Name=form_data['first_name'], LastName=form_data['last_name'])
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_user_details(user_id):
        try:
            user = Users.query.filter_by(Id=user_id).first()
            if not user:
                return None

            city = City.query.filter_by(CodeCity=user.NumCity).first()
            gender = Gender.query.filter_by(CodeGender=user.Gender).first()
            level_start = LevelStart.query.filter_by(CodeLevelStart=user.LevelStart).first()
            goal = Goal.query.filter_by(CodeGoal=user.Goal).first()
            trainer = Trainer.query.filter_by(CodeTrainer=user.Trainer).first()

            user_details = {
                'Name': user.Name,
                'LastName': user.LastName,
                'Phone': user.Pelepone,
                'City': city.NameCity if city else 'N/A',
                'Birthdate': user.Date,
                'Gender': gender.NameGender if gender else 'N/A',
                'Weight': user.Weight,
                'Height': user.Height,
                'LevelStart': level_start.NameLevelStart if level_start else 'N/A',
                'Goal': goal.NameGoal if goal else 'N/A',
                'Trainer': f"{trainer.Specialty} - {trainer.Description}" if trainer else 'N/A',
                'Rank': user.Rank,
                'Itkadmot': user.Itkadmot
            }

            return user_details

        except SQLAlchemyError as e:
            raise Exception(f"Database error: {str(e)}")
