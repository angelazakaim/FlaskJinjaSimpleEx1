# Client Controller - All business logic
from flask import render_template, request, redirect, url_for
from database import db
from models.client import Client


# READ - List all clients
def list_clients_action():
    all_clients = Client.query.all()
    print(f"DEBUG: Found {len(all_clients)} clients")  # Add this
    print(f"DEBUG: Clients exist? {bool(all_clients)}")  # Add this
    return render_template(
        'clients/clients.html',
        clients=all_clients,
        page_title="Clients"
    )

# READ - View single client details
def details_client_action(id):
    client = Client.query.get_or_404(id)
    return render_template(
        "clients/details.html",
        client=client,
        page_title="Client Details"
    )


# CREATE - Show add form (GET)
def show_add_client_form():
    return render_template(
        'clients/add.html',
        page_title="Add Client"
    )


# CREATE - Process add form (POST)
def add_client_action():
    new_client = Client(
        firstname=request.form['first_name'],
        lastname=request.form['last_name'],
        email=request.form['email'],
        tel=request.form['tel'],
        identification_number=request.form['id_num']
    )
    db.session.add(new_client)
    db.session.commit()
    return redirect(url_for('clients_bp.list_clients_route'))


# UPDATE - Show edit form (GET) and process update (POST)
def update_client_action(id):
    client = Client.query.get_or_404(id)

    if request.method == 'POST':
        client.firstname = request.form['first_name']
        client.lastname = request.form['last_name']
        client.email = request.form['email']
        client.tel = request.form['tel']
        client.identification_number = request.form['id_num']
        db.session.commit()
        return redirect(url_for('clients_bp.list_clients_route'))

    return render_template(
        'clients/edit.html',
        client=client,
        page_title="Edit Client"
    )


# DELETE - Delete a client
def delete_client_action(id):
    client = Client.query.get_or_404(id)
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for('clients_bp.list_clients_route'))