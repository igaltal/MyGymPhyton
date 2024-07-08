from app import db
from app.models import Level, LevelStart, Users, Trainer, City
from sqlalchemy.exc import SQLAlchemyError


def add_levels():
    levels = [
        Level(CodeLevel=1, NameLevel="Beginner"),
        Level(CodeLevel=2, NameLevel="Intermediate"),
        Level(CodeLevel=3, NameLevel="Getting There"),
        Level(CodeLevel=4, NameLevel="In Good Pace"),
        Level(CodeLevel=5, NameLevel="Regular Champion")
    ]
    try:
        db.session.bulk_save_objects(levels)
        db.session.commit()
        print("Levels added successfully.")
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error adding levels: {str(e)}")

def add_level_starts():
    level_starts = [
        LevelStart(CodeLevelStart=1, NameLevelStart="Beginner"),
        LevelStart(CodeLevelStart=2, NameLevelStart="Intermediate"),
        LevelStart(CodeLevelStart=3, NameLevelStart="Getting There"),
        LevelStart(CodeLevelStart=4, NameLevelStart="In Good Pace"),
        LevelStart(CodeLevelStart=5, NameLevelStart="Regular Champion")
    ]
    try:
        db.session.bulk_save_objects(level_starts)
        db.session.commit()
        print("Level starts added successfully.")
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error adding level starts: {str(e)}")

def add_trainers_and_users():
    trainers = [
        Users(Id=1, Name="איתי", LastName="כהן", Pelepone="0501234567", NumCity=1, Thisdata="01/01/1980", Password="password", Date="01/01/1980", Gender=1, Weight=75, Height=180, LevelStart=3, Goal=1, Trainer=True, Rank=1, Itkadmot=0),
        Users(Id=2, Name="שירה", LastName="לוי", Pelepone="0502345678", NumCity=2, Thisdata="02/02/1982", Password="password", Date="02/02/1982", Gender=2, Weight=60, Height=170, LevelStart=3, Goal=2, Trainer=True, Rank=1, Itkadmot=0),
        Users(Id=3, Name="יובל", LastName="אברהם", Pelepone="0503456789", NumCity=3, Thisdata="03/03/1983", Password="password", Date="03/03/1983", Gender=1, Weight=80, Height=175, LevelStart=4, Goal=3, Trainer=True, Rank=2, Itkadmot=0),
        Users(Id=4, Name="נועה", LastName="רוזן", Pelepone="0504567890", NumCity=4, Thisdata="04/04/1984", Password="password", Date="04/04/1984", Gender=2, Weight=65, Height=165, LevelStart=2, Goal=1, Trainer=True, Rank=2, Itkadmot=0),
        Users(Id=5, Name="אורן", LastName="מזרחי", Pelepone="0505678901", NumCity=5, Thisdata="05/05/1985", Password="password", Date="05/05/1985", Gender=1, Weight=78, Height=185, LevelStart=5, Goal=2, Trainer=True, Rank=3, Itkadmot=0),
        Users(Id=6, Name="הילה", LastName="בן דוד", Pelepone="0506789012", NumCity=6, Thisdata="06/06/1986", Password="password", Date="06/06/1986", Gender=2, Weight=55, Height=160, LevelStart=1, Goal=1, Trainer=True, Rank=1, Itkadmot=0),
        Users(Id=7, Name="ליאור", LastName="כהן", Pelepone="0507890123", NumCity=7, Thisdata="07/07/1987", Password="password", Date="07/07/1987", Gender=1, Weight=82, Height=175, LevelStart=3, Goal=3, Trainer=True, Rank=2, Itkadmot=0),
        Users(Id=8, Name="דנה", LastName="שרון", Pelepone="0508901234", NumCity=8, Thisdata="08/08/1988", Password="password", Date="08/08/1988", Gender=2, Weight=68, Height=168, LevelStart=4, Goal=2, Trainer=True, Rank=2, Itkadmot=0),
        Users(Id=9, Name="תומר", LastName="חדד", Pelepone="0509012345", NumCity=9, Thisdata="09/09/1989", Password="password", Date="09/09/1989", Gender=1, Weight=77, Height=180, LevelStart=2, Goal=1, Trainer=True, Rank=3, Itkadmot=0),
        Users(Id=10, Name="רונית", LastName="גפן", Pelepone="0500123456", NumCity=10, Thisdata="10/10/1990", Password="password", Date="10/10/1990", Gender=2, Weight=60, Height=170, LevelStart=5, Goal=2, Trainer=True, Rank=1, Itkadmot=0)
    ]

    try:
        db.session.bulk_save_objects(trainers)
        db.session.commit()
        print("Trainers and users added successfully.")
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error adding trainers and users: {str(e)}")

    trainers_details = [
        Trainer(CodeTrainer=1, Specialty="Strength Training", Description="Expert in muscle building"),
        Trainer(CodeTrainer=2, Specialty="Cardio", Description="Specializes in cardiovascular health"),
        Trainer(CodeTrainer=3, Specialty="Pilates", Description="Certified Pilates instructor"),
        Trainer(CodeTrainer=4, Specialty="Yoga", Description="Yoga master with 10 years of experience"),
        Trainer(CodeTrainer=5, Specialty="Weight Loss", Description="Helps clients achieve weight loss goals"),
        Trainer(CodeTrainer=6, Specialty="CrossFit", Description="CrossFit coach and competitor"),
        Trainer(CodeTrainer=7, Specialty="Aerobics", Description="Aerobics instructor with high energy classes"),
        Trainer(CodeTrainer=8, Specialty="Boxing", Description="Boxing coach with professional experience"),
        Trainer(CodeTrainer=9, Specialty="Swimming", Description="Certified swimming coach"),
        Trainer(CodeTrainer=10, Specialty="Martial Arts", Description="Expert in various martial arts disciplines")
    ]

    try:
        db.session.bulk_save_objects(trainers_details)
        db.session.commit()
        print("Trainers details added successfully.")
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error adding trainers details: {str(e)}")

def add_cities():
    cities = [
        City(CodeCity=1, NameCity="Tel Aviv"),
        City(CodeCity=2, NameCity="Jerusalem"),
        City(CodeCity=3, NameCity="Haifa"),
        City(CodeCity=4, NameCity="Rishon LeZion"),
        City(CodeCity=5, NameCity="Petah Tikva"),
        City(CodeCity=6, NameCity="Ashdod"),
        City(CodeCity=7, NameCity="Netanya"),
        City(CodeCity=8, NameCity="Beer Sheva"),
        City(CodeCity=9, NameCity="Bnei Brak"),
        City(CodeCity=10, NameCity="Holon"),
        City(CodeCity=11, NameCity="Ramat Gan"),
        City(CodeCity=12, NameCity="Ashkelon"),
        City(CodeCity=13, NameCity="Rehovot"),
        City(CodeCity=14, NameCity="Bat Yam"),
        City(CodeCity=15, NameCity="Kfar Saba"),
        City(CodeCity=16, NameCity="Herzliya"),
        City(CodeCity=17, NameCity="Hadera"),
        City(CodeCity=18, NameCity="Modiin"),
        City(CodeCity=19, NameCity="Nazareth"),
        City(CodeCity=20, NameCity="Raanana"),
        City(CodeCity=21, NameCity="Rosh HaAyin"),
        City(CodeCity=22, NameCity="Lod"),
        City(CodeCity=23, NameCity="Kiryat Ata"),
        City(CodeCity=24, NameCity="Givatayim"),
        City(CodeCity=25, NameCity="Eilat"),
        City(CodeCity=26, NameCity="Ramat Hasharon"),
        City(CodeCity=27, NameCity="Afula"),
        City(CodeCity=28, NameCity="Yehud"),
        City(CodeCity=29, NameCity="Nahariya"),
        City(CodeCity=30, NameCity="Beit Shemesh")
    ]

    try:
        db.session.bulk_save_objects(cities)
        db.session.commit()
        print("Cities added successfully.")
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error adding cities: {str(e)}")
