# app.py
import os
import logging
from flask import Flask, render_template, request
from dotenv import load_dotenv


# Load .env ONLY for local development
if os.environ.get("FLASK_ENV") != "production":
    load_dotenv()

# Imports AFTER env vars are loaded
from config import config_map
from database import db , migrate
from models import Client, Car
from routes.client_routes import clients_bp
from routes.car_routes import cars_bp


def create_app():
    # Determine environment
    env = os.environ.get("FLASK_ENV") or "development"

    # Select config
    config_class = config_map.get(env)
    if not config_class:
        raise RuntimeError(f"Invalid FLASK_ENV: {env}")

    # Create app
    app = Flask(__name__)
    app.config.from_object(config_class)
    config_class.validate()

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    @app.before_request
    def log_request():
        logging.info("%s %s", request.method, request.path)

    # Blueprints
    app.register_blueprint(clients_bp, url_prefix="/clients")
    app.register_blueprint(cars_bp, url_prefix="/cars")

    # Routes
    @app.route("/")
    def index():
        return render_template("index.html", page_title="Garage Management")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
