from app import db

class City(db.Model):
    __tablename__ = 'Cities'
    CodeCity = db.Column(db.Integer, primary_key=True)
    NameCity = db.Column(db.String, nullable=False)

class Exercise(db.Model):
    __tablename__ = 'Exercises'
    NumberExercises = db.Column(db.Integer, primary_key=True)
    NameExercises = db.Column(db.String, nullable=False)
    Description = db.Column(db.Text)
    WorkOn = db.Column(db.Integer)
    levelThis = db.Column(db.Integer)

class ExercisesTrain(db.Model):
    __tablename__ = 'ExercisesTrain'
    CodeCoaching = db.Column(db.Integer, primary_key=True)
    CodeExercises = db.Column(db.Integer, primary_key=True)
    NumBack = db.Column(db.String)
    RetaNumber = db.Column(db.String)
    WorkOnCode = db.Column(db.Integer)

class Gender(db.Model):
    __tablename__ = 'Gender'
    CodeGender = db.Column(db.Integer, primary_key=True)
    NameGender = db.Column(db.String, nullable=False)

class Goal(db.Model):
    __tablename__ = 'Goal'
    CodeGoal = db.Column(db.Integer, primary_key=True)
    NameGoal = db.Column(db.String, nullable=False)

class Level(db.Model):
    __tablename__ = 'Levels'
    CodeLevel = db.Column(db.Integer, primary_key=True)
    NameLevel = db.Column(db.String, nullable=False)

class LevelStart(db.Model):
    __tablename__ = 'LevelStart'
    CodeLevelStart = db.Column(db.Integer, primary_key=True)
    NameLevelStart = db.Column(db.String, nullable=False)

class Message(db.Model):
    __tablename__ = 'Messages'
    Froms = db.Column(db.Integer, primary_key=True)
    To = db.Column(db.Integer)
    Date = db.Column(db.String)
    TheMessage = db.Column(db.Text)

class Presence(db.Model):
    __tablename__ = 'Presence'
    UserId = db.Column(db.Integer, primary_key=True)
    NumberOF = db.Column(db.Integer)
    From = db.Column(db.String)
    To = db.Column(db.String)

class Rank(db.Model):
    __tablename__ = 'Ranks'
    RankCode = db.Column(db.Integer, primary_key=True)
    RankName = db.Column(db.String, nullable=False)

class Trainer(db.Model):
    __tablename__ = 'Trainers'
    CodeTrainer = db.Column(db.Integer, db.ForeignKey('Users.Id'), primary_key=True)
    Specialty = db.Column(db.String, nullable=False)
    Description = db.Column(db.Text, nullable=False)

class Users(db.Model):
    __tablename__ = 'Users'
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    Pelepone = db.Column(db.String(50))  
    NumCity = db.Column(db.Integer)
    Thisdata = db.Column(db.String(50)) 
    Password = db.Column(db.String(50))
    Date = db.Column(db.String(50))
    Gender = db.Column(db.Integer)
    Weight = db.Column(db.Integer)
    Height = db.Column(db.Integer)
    LevelStart = db.Column(db.Integer)
    LevelNow = db.Column(db.Integer)
    Goal = db.Column(db.Integer)
    Trainer = db.Column(db.Boolean)  
    Rank = db.Column(db.Integer)
    Itkadmot = db.Column(db.Integer)


class WeightHeight(db.Model):
    __tablename__ = 'WeightHeight'
    Id = db.Column(db.Integer, primary_key=True)
    DateWeight = db.Column(db.String, primary_key=True)
    NumberOf = db.Column(db.Integer, primary_key=True)
    Weight = db.Column(db.Integer)
    Height = db.Column(db.Integer)

class WorkOnTa(db.Model):
    __tablename__ = 'WorkOnTa'
    CodeWork = db.Column(db.Integer, primary_key=True)
    NameWork = db.Column(db.String, nullable=False)

