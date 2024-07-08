from app import db
from app.models import WeightHeight
from sqlalchemy.exc import SQLAlchemyError
from app.models import Users


class WeightService:
    @staticmethod
    def get_all_weight(user_id):
        try:
            return WeightHeight.query.filter_by(user_id=user_id).all()
        except SQLAlchemyError as e:
            raise Exception(f"Database error occurred: {str(e)}")

    @staticmethod
    def insert_weight(user_id, weight, height, date, number):
        try:
            new_weight = WeightHeight(user_id=user_id, weight=weight, height=height, date=date, number=number)
            db.session.add(new_weight)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Database error occurred: {str(e)}")

    @staticmethod
    def check_date(date):
        try:
            return WeightHeight.query.filter_by(date=date).all()
        except SQLAlchemyError as e:
            raise Exception(f"Database error occurred: {str(e)}")
