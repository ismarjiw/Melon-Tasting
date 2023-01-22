import os
from random import choice, randint
from datetime import datetime, date, time

import crud
from model import User, Reservation, Appointment, connect_to_db, db
import server

os.system("dropdb meditations")
os.system('createdb meditations')

connect_to_db(server.app, "melons")
db.create_all()

user1 = User (
    username = 'mint'
)

user2 = User (
    username = 'chocolate'
)

user3 = User (
    username = 'vanilla'
)

res1 = Reservation (
    user_id = 1,
    length = 30,
    date = datetime.now()
)

res2 = Reservation (
    user_id = 2,
    length = 30,
    date = datetime.now()
)

res3 = Reservation (
    user_id = 3,
    length = 30,
    date = datetime.now()
)

apt1 = Appointment(
    length=30, 
    date=date(2023, 1, 21), 
    start_time=time(9,0), 
    end_time=time(9,30))

apt2 = Appointment(
    length=30, 
    date=date(2023, 1, 21), 
    start_time=time(9,30), 
    end_time=time(10,0))

apt3 = Appointment(
    length=30, 
    date=date(2023, 1, 21), 
    start_time=time(10,0), 
    end_time=time(10,30))

db.session.add_all([user1, user2, user3, res1, res2, res3, apt1, apt2, apt3])
db.session.commit()