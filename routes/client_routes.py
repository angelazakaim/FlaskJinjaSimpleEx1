from flask import Blueprint, render_template, request, redirect, url_for
from models import db
from models.client import Client

# Define the blueprint
clients_bp = Blueprint('clients', __name__)


# This now maps to /clients/
@clients_bp.route('/', methods=['GET', 'POST'])
def list_clients():
    if request.method == 'POST':
        new_c = Client(
            firstname=request.form['firstname'],
            lastname=request.form['lastname'],
            email=request.form['email'],
            tel=request.form['tel'],
            identification_number=request.form['id_num']
        )
        db.session.add(new_c)
        db.session.commit()
        return redirect(url_for('clients.list_clients'))
    
    clients = Client.query.all()
    return render_template('clients/list.html', clients=clients)

@clients_bp.route('/delete/<int:id>')
def delete(id):
    client = Client.query.get_or_404(id)
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for('clients.list_clients'))


