from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash
from .AdminUser import AdminUser
from .Reservation import Reservation
from .forms import *


#@app.route("/", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def user_options():
    
    form = UserOptionForm()
    if request.method == 'POST' and form.validate_on_submit():
        option = request.form['option']

        if option == "1":
            return redirect('/admin')
        else:
            return redirect("/reservations")
    
    return render_template("options.html", form=form, template="form-template")

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    form = AdminLoginForm()

    errors = []
    total_sales = False
    seating_chart = []
    if request.method == 'POST' and form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        login = AdminUser(username, password)
        if login.is_registered():
            total_sales = Reservation.get_total_sales()
            reservations = Reservation.get_all()
            seating_chart = [['O', 'O', 'O', 'O'] for _ in range(12)]
            for r in reservations:
                seating_chart[r[0]][r[1]] = "X"
        else:
            errors.append('Bad username/password combination. Try again.')

    return render_template("admin.html", form=form, template="form-template", errors=errors, total_sales=total_sales, seating_chart=seating_chart)

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():

    form = ReservationForm()

    return render_template("reservations.html", form=form, template="form-template")

