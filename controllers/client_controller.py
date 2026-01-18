from flask import render_template, request, redirect, url_for
from database import db
from models.client import Client

# READ (All)
def list_clients_action():
    clients = Client.query.all()
    return render_template('clients/list.html', clients=clients)

# CREATE
def add_client_action():
    new_client = Client(
        firstname=request.form['firstname'],
        lastname=request.form['lastname'],
        email=request.form['email'],
        tel=request.form['tel'],
        identification_number=request.form['id_num']
    )
    db.session.add(new_client)
    db.session.commit()
    return redirect(url_for('clients_bp.list_clients_route'))

# UPDATE (GET form & POST update)
def update_client_action(id):
    client = Client.query.get_or_404(id)
    if request.method == 'POST':
        client.firstname = request.form['firstname']
        client.lastname = request.form['lastname']
        client.email = request.form['email']
        client.tel = request.form['tel']
        client.identification_number = request.form['id_num']
        db.session.commit()
        return redirect(url_for('clients_bp.list_clients_route'))
    
    return render_template('clients/edit.html', client=client)

# DELETE
def delete_client_action(id):
    client = Client.query.get_or_404(id)
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for('clients_bp.list_clients_route'))