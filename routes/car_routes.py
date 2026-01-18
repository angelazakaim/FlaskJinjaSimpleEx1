# 5. The URL: Routing (Example: Car)
# The Blueprint only maps the URL to the Controller.
from flask import Blueprint, request
from controllers import car_controller

cars_bp = Blueprint('cars_bp', __name__)


# List all cars (GET only)
@cars_bp.route('/', methods=['GET'])
def list_cars_route():
    return car_controller.list_cars_action()


# Show add form (GET) and process submission (POST)
@cars_bp.route('/add', methods=['GET', 'POST'])
def add_car_route():
    if request.method == 'POST':
        return car_controller.add_car_action()
    return car_controller.show_add_car_form()


# View car details
@cars_bp.route('/details/<int:id>', methods=['GET'])
def view_car_details(id):
    return car_controller.details_car_action(id)


# Edit car (Handles both GET to show form and POST to save)
@cars_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_car_route(id):
    return car_controller.update_car_action(id)


# Delete car
@cars_bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_car_route(id):
    return car_controller.delete_car_action(id)