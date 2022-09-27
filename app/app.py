 
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

app.config['SECRET_KEY'] = '3544fe8c6d3b44ecb82e1f4670ae2e4f'

db = SQLAlchemy(app)