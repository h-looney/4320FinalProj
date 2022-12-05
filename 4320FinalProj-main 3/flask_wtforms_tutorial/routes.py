from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash
from .AdminUser import AdminUser
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
    if request.method == 'POST' and form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        login = AdminUser(username=username, password=password)
        if login.is_registered():
            return redirect('/admin/datashowcase')
        else:
            print("not certified")

    return render_template("admin.html", form=form, template="form-template")

        

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():
    form = ReservationForm()
    return render_template("reservations.html", form=form, template="form-template")


@app.route("/admin/datashowcase", methods=['GET', 'POST'])
def datashowcase():
    form = AdminDataShowcase()

    return render_template("data_display.html", form=form, template="form-template")
