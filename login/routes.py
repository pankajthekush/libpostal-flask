from posixpath import abspath
import flask_login
from flask_login import login_user, login_required, LoginManager
from app import app
from flask import Blueprint, render_template, redirect, request
import os
from werkzeug.security import check_password_hash
from .models import Users
from .forms import LoginForm


login_manager = LoginManager()
login_manager.init_app(app=app)

@login_manager.user_loader
def user_loader(id):
    return Users.query.get(int(id))

api_login = Blueprint('login',__name__)


@api_login.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if (user is not None) and check_password_hash(user.password ,form.password.data):
            login_user(user=user, remember=True)
            return 'success'
        else:
            return 'fail'
        
    return render_template('login.html', form=form)

login_manager.unauthorized_handler
def unauth_handler():
    return redirect('login')