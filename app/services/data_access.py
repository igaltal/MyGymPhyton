# /app/services/data_access.py
from app import db
from app.models.models import City

from app.models.models import Users

def get_cities():
    return City.query.all()


def get_account_by_credentials(user_id, user_password):
    return Users.query.filter_by(Id=user_id, Password=user_password).first()
