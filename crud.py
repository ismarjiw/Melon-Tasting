from model import db, User, Reservation, Appointment, connect_to_db
from flask import json
from datetime import *
from sqlalchemy import desc

def create_user(username):
    """Create and return a new user"""

    user = User(username=username)

    return user

def get_users():
    """Return all users"""

    return User.query.all()

def get_user_by_id(user_id):
    """Return a user by primary key"""

    return User.query.get(user_id)

def get_user_by_username(username):
    """Return a user by username"""

    return User.query.filter(User.username == username).first()

def create_reservation(user_id, appointment_id, length, date):
    """Create and return a reservation"""

    reservation = Reservation(
        user_id=user_id,
        appointment_id=appointment_id,
        length=length,
        date=date
    )

    return reservation 

def get_reservation_by_id(reservation_id):
    """Return reservation by id"""

    return Reservation.query.get(reservation_id)

def get_reservation_by_user_id(user_id):
    """Return all reservations by user id"""

    return Reservation.query.get(user_id)

def get_all_reservations():
    """Return all reservations"""

    return Reservation.query.all()

def get_all_appointments():
    """Return all appointments"""

    return Appointment.query.all()

def get_appointment_by_id(appointment_id):
    """Return appointment by id"""

    return Appointment.query.get(appointment_id)

if __name__ == '__main__':
    from server import app
    connect_to_db(app, "melons")