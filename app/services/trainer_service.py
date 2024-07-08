from app import db
from app.models import Users, Trainer
from sqlalchemy.exc import SQLAlchemyError

def get_trainers():
    try:
        return Trainer.query.join(Users).all()
    except SQLAlchemyError as e:
        raise Exception(f"Database error: {str(e)}")

def get_trainer_by_id(trainer_id):
    try:
        return Trainer.query.join(Users).filter(Users.id == trainer_id).first()
    except SQLAlchemyError as e:
        raise Exception(f"Database error: {str(e)}")

def add_new_trainer(id, specialty, description):
    try:
        new_trainer = Trainer(id=id, specialty=specialty, description=description)
        db.session.add(new_trainer)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise Exception(f"Database error: {str(e)}")

def get_trainers_for_messaging():
    try:
        return Users.query.filter_by(rank=1).all()
    except SQLAlchemyError as e:
        raise Exception(f"Database error: {str(e)}")
