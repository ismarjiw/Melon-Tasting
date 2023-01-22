from model import db, User, Reservation, connect_to_db
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

def get_user_by_un(username):
    """Return a user by username"""

    return User.query.filter(User.username == username).first()

def create_reservation(user_id, length, date):
    """Create and return a reservation"""

    reservation = Reservation(
        user_id=user_id,
        length=length,
        date=date
    )

    return reservation 

def get_reservation_by_id(reservation_id):
    """Return reservation by id"""

    return Reservation.query.get(reservation_id)

def get_all_reservations():
    """Return all reservations"""

    return Reservation.query.all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)