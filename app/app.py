 
from flask import Flask,render_template,request
from .hfunc import PG_CONN_STR
from flask_sqlalchemy import SQLAlchemy
import os

static_dir = os.path.abspath('./static')
template_dir = os.path.abspath('./templates')

app = Flask(__name__,static_folder=static_dir,template_folder=template_dir)

app.config['CORS_HEADERS'] = 'Content-Type'

app.config['SQLALCHEMY_DATABASE_URI'] = PG_CONN_STR
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# change secrect key

app.config['SECRET_KEY'] = os.environ['SECRECT_KEY']

db = SQLAlchemy(app)