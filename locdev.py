from flask import Flask
from app import app,db
from login import api_login
from login import create_new_user

app.register_blueprint(api_login)
db.create_all()



if __name__ == '__main__':

    # create_new_user('test@test.com','123321')
     app.run(debug=True)