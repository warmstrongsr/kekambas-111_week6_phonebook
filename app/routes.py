from app import app, db
from flask import render_template, redirect, url_for, flash
from app.models import Address
from app.forms import AddressForm


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', name='Will')
    
@app.route('/address/', methods=['GET','POST'])
def address():
    form = AddressForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        address = form.address.data
        phone = form.phone.data
        print(first_name, last_name, address, phone)
         # Check to see if there is already a user with either username or email
        check_address = Address.query.filter((Address.phone == phone) | (Address.address == address)).all()
        if check_address:
            # Flash a message saying that user with email/username already exists
            flash("A user with that username and/or email already exists", "warning")
            return redirect(url_for('address'))
        # If check_user is empty, create a new record in the user table
        new_address = Address(first_name=first_name, last_name=last_name, phone=phone, address=address)
        flash(f"Thank you {first_name}, for signing up!", "success")
        return redirect(url_for('index'))
    return render_template('address.html', form=form)













# @app.route('/login', methods=["GET", "POST"])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         form = LoginForm()
#         email = form.email.data
#         username = form.username.data
#         password = form.password.data
#         print(email, username, password)
#         flash(f"Thank you {username} for signing in!", "success")
#         return redirect(url_for('index'))
#     return render_template('login.html', form=form)