# 6. The Models Folder
# Each file starts with from database import db.
from database import db
from .status_enum import WorkStatus

class Car(db.Model):

#without this line table will be called lower case of the model: car
    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key=True)
    plate_number = db.Column(db.String(20), unique=True)
    year = db.Column(db.Integer)
    brand = db.Column(db.String(50))
    model = db.Column(db.String(50))
    color = db.Column(db.String(20))
    status = db.Column(db.Enum(WorkStatus))
    image_path = db.Column(db.String(50))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))