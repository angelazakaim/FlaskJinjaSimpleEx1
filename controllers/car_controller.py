# 4. The Logic: Controller Action (Example: Car)
# Separating the logic ensures your routes stay clean.
from flask import render_template, request, redirect, url_for
from database import db
from models.car import Car
from models.client import Client
from models.status_enum import WorkStatus


# READ - List all cars
def list_cars_action():
    all_cars = Car.query.all()
    return render_template(
        'cars/cars.html', 
        cars=all_cars, 
        page_title="Cars"
    )


# READ - View single car details
def details_car_action(id):
    car = Car.query.get_or_404(id)
    return render_template(
        "cars/details.html",
        car=car,
        page_title="Car Details"
    )


# CREATE - Show add form (GET)
def show_add_car_form():
    all_clients = Client.query.all()
    return render_template(
        'cars/add.html', 
        clients=all_clients, 
        statuses=WorkStatus, 
        page_title="Add Car"
    )


# CREATE - Process add form (POST)
def add_car_action():
    new_car = Car(
        plate_number=request.form['plate_number'],
        year=int(request.form['year']),
        brand=request.form['brand'],
        model=request.form['model'],
        color=request.form['color'],
        status=WorkStatus(request.form['status']),
        client_id=request.form['client_id']
    )
    db.session.add(new_car)
    db.session.commit()
    return redirect(url_for('cars_bp.list_cars_route'))


# UPDATE - Show edit form (GET) and process update (POST)
def update_car_action(id):
    car = Car.query.get_or_404(id)
    clients = Client.query.all()
    
    if request.method == 'POST':
        car.plate_number = request.form['plate_number']
        car.year = int(request.form['year'])
        car.brand = request.form['brand']
        car.model = request.form['model']
        car.color = request.form['color']
        car.status = WorkStatus(request.form['status'])
        car.owner.firstname = request.form['owner_first_name']
        car.owner.lastname = request.form['owner_last_name']
        car.owner.email = request.form['owner_email']
        db.session.commit()
        return redirect(url_for('cars_bp.list_cars_route'))
    
    return render_template(
        'cars/edit.html', 
        car=car, 
        clients=clients, 
        statuses=WorkStatus,
        page_title="Edit Car"
    )


# DELETE - Delete a car
def delete_car_action(id):
    car = Car.query.get_or_404(id)
    db.session.delete(car)
    db.session.commit()
    return redirect(url_for('cars_bp.list_cars_route'))