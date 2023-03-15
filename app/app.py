 
from flask import Flask,request
import os


app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'


app.config['SECRET_KEY'] = '3544fe8c6d3b44ecb82e1f4670ae2e4f'
