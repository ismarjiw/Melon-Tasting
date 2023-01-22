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

    user = crud.get_user_by_un(username=username)

    if user:
        session["username"] = username
        session["user_id"] = user.user_id
        return redirect("/make_reservation")
    else:
        flash("Incorrect username. Please try again.")
        return redirect("/login")

@app.route("/make_reservation")
def reservation_page():
    """Reservation page"""

    if 'user_id' not in session: 
        return redirect("/login")

    user = crud.get_user_by_id(session["user_id"])

    return render_template("reservation.html")

@app.route("/logout")
def logout():
    """Logs out user"""

    session.pop('user_id', None)

    return redirect('/')

if __name__ == "__main__":
    connect_to_db(app, "melons")
    app.run(host="0.0.0.0", debug=True)