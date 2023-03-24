from app import app, db
from flask import render_template, redirect, url_for, flash
from app.models import Address, User
from app.forms import AddressForm, LoginForm, SignUpForm
from flask_login import login_required, current_user, logout_user, login_user


@app.route('/', methods=["GET"])
def index():
    addresses = Address.query.all()
    return render_template('index.html', addresses=addresses)
    
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('Form is valid')
        username = form.username.data
        password = form.password.data
        print(username, password)
        # Check if there is a user with this username and password in the database already
        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            # If a user with this username and password, allow the login to proceed
            login_user(user)
            flash(f'You have logged in sucessfully, {username}', 'success')
            return redirect(url_for('login'))
        
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("You have logged out", "info")
    return redirect(url_for('index'))


@app.route('/create', methods=["GET", "POST"])
@login_required
def create_address():
    form = AddressForm()
    if form.validate_on_submit():
        # Get the data from the form
        first_name = form.first_name.data
        last_name = form.last_name.data
        address = form.address.data
        phone = form.phone.data
        # Create an instance of Post with form data AND auth user ID
        new_address = Address(first_name=first_name, last_name=last_name, phone=phone, address=address)
        flash(f"{new_address.title} has been created!", "success")
        return redirect(url_for('index'))
    return render_template('create.html', form=form)

@app.route('/address/', methods=["GET","POST"])
def address():
    form = AddressForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        address = form.address.data
        phone = form.phone.data
        print(first_name, last_name, address, phone)
        # If check_user is empty, create a new record in the user table
        new_address = Address(first_name=first_name, last_name=last_name, phone=phone, address=address)
        flash(f"Thank you {first_name}, {new_address} has been added successfully!", "success")
        return redirect(url_for('index'))
    return render_template('address.html', form=form)

@app.route('/edit/<address_id>', methods=["GET", "POST"])
@login_required
def edit_address(address_id):
    form = AddressForm()
    address_to_edit = Address.query.get_or_404(address_id)
    # Make sure that the address author is the current user
    if address_to_edit.author != current_user:
        flash("You do not have permission to edit this post", "danger")
        return redirect(url_for('index'))

    # If form submitted, update Address
    if form.validate_on_submit():
        # update the post with the form data
        address_to_edit.title = form.first_name.data
        address_to_edit.body = form.last_name.data
        address_to_edit.phone = form.phone.data
        address_to_edit.address = form.address.data
        # Commit that to the database
        db.session.commit()
        flash(f"{address_to_edit.title} has been edited!", "success")
        return redirect(url_for('index'))

    # Pre-populate the form with Post To Edit's values
    form.first_name.data = address_to_edit.title
    form.last_name.data = address_to_edit.body
    form.phone.data = address_to_edit.image_url
    form.address.data = address_to_edit.image_url
    return render_template('edit.html', form=form, post=address_to_edit)


@app.route('/delete/<address_id>')
@login_required
def delete_address(address_id):
    address_to_delete = Address.query.get_or_404(address_id)
    if address_to_delete.author != current_user:
        flash("You do not have permission to delete this post", "danger")
        return redirect(url_for('index'))

    db.session.delete(address_to_delete)
    db.session.commit()
    flash(f"{address_to_delete.title} has been deleted", "info")
    return redirect(url_for('index'))


@app.route('/signup', methods=["GET", "POST"])
def signup():
    # Create an instance of the form (in the context of the current request)
    form = SignUpForm()
    # Check if the form was submitted and that all of the fields are valid
    if form.validate_on_submit():
        # If so, get the data from the form fields
        print('Hooray our form was validated!!')
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(first_name, last_name, email, username, password)
        # Check to see if there is already a user with either username or email
        check_user = db.session.execute(db.select(User).filter((User.username == username) | (User.email == email))).scalars().all()
        if check_user:
            # Flash a message saying that user with email/username already exists
            flash("A user with that username and/or email already exists", "warning")
            return redirect(url_for('signup'))
        # If check_user is empty, create a new record in the user table
        new_user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        flash(f"Thank you {new_user.username} for signing up!", "success")
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)
