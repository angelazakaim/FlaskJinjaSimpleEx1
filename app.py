# app.py
import os
import logging
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load environment variables FIRST, before any other imports
env = os.environ.get("FLASK_ENV", "development")
if env == "production":
    load_dotenv(".env.production", override=True)
else:
    load_dotenv(".env", override=True)

# NOW import config (after .env is loaded)
from config import config_map
from database import db
from models import Client, Car
from routes.client_routes import clients_bp
from routes.car_routes import cars_bp

def create_app():
    app = Flask(__name__)
    config_class = config_map[env]
    config_class.validate()  # Validate before loading
    app.config.from_object(config_class)
    db.init_app(app)

    # Logging middleware
    @app.before_request
    def log_action():
        logging.info(f"{request.method} {request.path}")

    # Blueprints
    app.register_blueprint(clients_bp, url_prefix="/clients")
    app.register_blueprint(cars_bp, url_prefix="/cars")

    # DEV tables
    if env == "development":
        with app.app_context():
            db.create_all()

    # Routes
    @app.route("/")
    def index():
        return render_template("index.html", page_title="Garage Management")

    @app.route("/clients")
    def clients():
        clients = Client.query.all()
        return render_template(
            "clients/clients.html",
            clients=clients,
            page_title="Clients"
        )

    return app

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run()
