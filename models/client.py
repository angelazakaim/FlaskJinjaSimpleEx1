from database import db

class Client(db.Model):

#without this line table will be called lower case of the model: client
    __tablename__ = "clients"


    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tel = db.Column(db.String(20), nullable=False)
    identification_number = db.Column(db.String(20), unique=True, nullable=False)
    
    # Relationship: One client can have many cars
    cars = db.relationship('Car', backref='owner', cascade="all, delete-orphan", lazy=True)