from app import db
from flask_login import UserMixin


class Users( UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    is_admin = db.Column(db.Boolean)
    is_active = db.Column(db.Boolean)
    company = db.Column(db.String)
