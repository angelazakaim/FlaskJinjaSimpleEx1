# Import the SQLAlchemy instance and the Models
from .client import db, Client
from .car import Car
from .status_enum import WorkStatus

# This makes it easier to import everything at once in app.py:
# From: from models import db, Client, Car