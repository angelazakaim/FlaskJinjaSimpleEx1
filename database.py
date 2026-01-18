# 2. The Database Initialization
# We keep the db object in its own file to prevent "Circular Imports" (when two files try to import each other).
from flask_sqlalchemy import SQLAlchemy

# Globally accessible database object
db = SQLAlchemy()