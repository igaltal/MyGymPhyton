from app import create_app, db
from app.models import Users, Trainer, City, Level, LevelStart
from app.services.data_population import add_levels, add_level_starts, add_trainers_and_users, add_cities


app = create_app()

with app.app_context():
    db.create_all()
    print("Database tables created successfully.")

if __name__ == '__main__':
    app.run(debug=True)

