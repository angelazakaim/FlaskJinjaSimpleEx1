# Client Routes Blueprint
from flask import Blueprint, request
from controllers import client_controller

clients_bp = Blueprint('clients_bp', __name__)


# List all clients (GET only)
@clients_bp.route('/', methods=['GET'])
def list_clients_route():
    return client_controller.list_clients_action()


# Show add form (GET) and process submission (POST)
@clients_bp.route('/add', methods=['GET', 'POST'])
def add_client_route():
    if request.method == 'POST':
        return client_controller.add_client_action()
    return client_controller.show_add_client_form()


# View client details
@clients_bp.route('/details/<int:id>', methods=['GET'])
def view_client_details(id):
    return client_controller.details_client_action(id)


# Edit client (Handles both GET to show form and POST to save)
@clients_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_client_route(id):
    return client_controller.update_client_action(id)


# Delete client
@clients_bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_client_route(id):
    return client_controller.delete_client_action(id)