from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date, time

db = SQLAlchemy()

class User(db.Model):
    """A user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    username = db.Column(db.String, unique=True)

    reservation = db.relationship("Reservation", uselist=False, back_populates="user")
    appointment = db.relationship("Appointment", uselist=False, back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} username={self.username}>"

class Reservation(db.Model):
    """A reservation"""

    __tablename__ = "reservations"

    reservation_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    appointment_id = db.Column(db.Integer, db.ForeignKey("appointments.appointment_id"))

    length = db.Column(db.Integer)
    date = db.Column(db.Date)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)

    user = db.relationship("User", uselist=False, back_populates="reservation")

    def __repr__(self):
        return f"<Reservation reservation_id={self.reservation_id} date={self.date}>"

class Appointment(db.Model):
    """Available appointments"""

    __tablename__ = "appointments"

    appointment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    reservation_id = db.Column(db.Integer, db.ForeignKey("reservations.reservation_id"))

    length = db.Column(db.Integer)
    date = db.Column(db.Date)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)

    user = db.relationship("User", uselist=False, back_populates="appointment")

    def __repr__(self):
        return f"<Appointment appointment_id={self.reservation_id} date={self.date}>"

def connect_to_db(app, db_name):
    """Connect to database"""

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app
    
    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.
    
    connect_to_db(app, "melons")