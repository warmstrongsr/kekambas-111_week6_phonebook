from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import UserInfoForm
from app.forms import LoginForm


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', name='Will')
    
@app.route('/users/', methods=['GET','POST'])
def users():
    form = UserInfoForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        address = form.address.data
        phone = form.phone.data
        print(first_name, last_name, address, phone)
        flash(f"Thank you {first_name}, for signing up!", "success")
        return redirect(url_for('index'))
    return render_template('users.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        form = LoginForm()
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(email, username, password)
        flash(f"Thank you {username} for signing in!", "success")
        return redirect(url_for('index'))
    return render_template('login.html', form=form)