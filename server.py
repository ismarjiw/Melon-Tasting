from flask import (Flask, render_template, request, flash, abort, session, redirect, Response, jsonify, json)
from model import connect_to_db, db
from jinja2 import StrictUndefined
from datetime import *
import crud 

app = Flask(__name__)
app.secret_key = "melon"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('index.html')

@app.route("/login")
def login_page():
    """Login page"""

    return render_template("login.html")

@app.route("/login", methods = ["POST"])
def user_login_page():
    """Logs in the user"""

    username = request.form.get("username")

    user = crud.get_user_by_username(username=username)

    if user:
        session["username"] = username
        session["user_id"] = user.user_id
        return redirect("/make_reservation")
    else:
        flash("Incorrect username. Please try again.")
        return redirect("/login")

@app.route("/make_reservation")
def reservation_page():
    """Make a reservation"""

    if 'user_id' not in session: 
        return redirect("/login")

    return render_template("reservation.html")

@app.route("/make_reservation", methods = ["POST"])
def search_appointments():
    """User checks if appointment is available for reservation"""

    requested_date = request.form.get("date")
    start_time = request.form.get("start-time")
    end_time = request.form.get("end-time")

    appointments = crud.get_all_appointments()

    date_object = date(*map(int, requested_date.split("-")))

    for appointment in appointments:
        if appointment.start_time == start_time:
            if appointment.end_time == end_time:
                if appointment.date == date_object:
                    return appointment
    
    return render_template("make_appointment.html", appointment=appointment)

@app.route("/make_appointment/<appointment>")
def make_appointment(appointment):
    """Page where users can save reservation of available appointments"""

    # why is appointment_id None on website but has appointment_id (1,2) in psql???
    # in interactive mode: 
    # [<Appointment appointment_id=None date=2023-01-21>, <Appointment appointment_id=None date=2023-01-21>]

    if appointment.appointment_id != None:
        reservation = crud.create_reservation(user_id=session["user_id"], appointment_id= appointment.appointment_id, length=30, date= appointment.date)
        db.session.add(reservation)
        print(reservation)
        print('*'*50)
        db.session.commit()
    else:
        return f"Unable to save reservation for selected appointment"

    return redirect("/reservations")

@app.route("/reservations")
def made_reservations():
    """User made reservations"""

    if 'user_id' in session:
        reservations = crud.get_reservation_by_user_id(session["user_id"])
    else:
        return redirect("/login")

    return render_template("all_reservations.html", reservations=reservations)

@app.route("/appointments")
def appointment_page():
    """Page with all available appointments"""

    appointments = crud.get_all_appointments()

    return render_template("appointments.html", appointments=appointments)

@app.route("/logout")
def logout():
    """Logs out user"""

    session.pop('user_id', None)

    return redirect('/')

if __name__ == "__main__":
    connect_to_db(app, "melons")
    app.run(host="0.0.0.0", debug=True)