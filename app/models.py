from app import db
from datetime import datetime
# from werkzeug.security import generate_password_hash, check_password_hash


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(25), nullable=False, unique=False)
    address = db.Column(db.String(75), nullable=False, unique=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.password = generate_password_hash(kwargs.get('password'))
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Address {self.id}|{self.username}>"

    # def check_password(self, password_guess):
    #     return check_password_hash(self.password, password_guess)
