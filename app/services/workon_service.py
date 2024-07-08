from app import db
from sqlalchemy.exc import SQLAlchemyError

def get_work_on():
    try:
        result = db.engine.execute("SELECT * FROM WorkOnTa")
        return [dict(row) for row in result]
    except SQLAlchemyError as e:
        raise Exception(f"Database error: {str(e)}")
