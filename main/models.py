from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users' # todo maybe rename the table name in our database, more natural
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))


# todo think about bringing in a confirmation email




