from .models import Users
from app import db
from werkzeug.security import generate_password_hash


def create_new_user(email,password):

    ##
    #first verify if user id already available
    ##
    user_id = db.session.query(Users.id).filter(Users.email == email).first()

    hash_password = generate_password_hash(password=password, method='sha256')
    new_user = Users(id = None if user_id is None else user_id.id, email=email, password=hash_password,is_active=True)
    db.session.merge(new_user)
    db.session.commit()
    return True