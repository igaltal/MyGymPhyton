from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/igaltal/Desktop/Degree/advanced_programing/projectIgalTal/Datatal.db'
    app.config['SECRET_KEY'] = b'v\x08\xf8\xdf\xf9\xd7D\xa6,\xe3\xed\x96\xab\x9c\xcf\x89m\xc7\xaa9\x95\x9f\x7f\xa4'

    from app.routes.user_routes import user_bp
    from app.routes.views import bp as views_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(views_bp)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
