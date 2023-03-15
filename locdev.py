from flask import Flask
from app import app
from api_postal import api_postal
app.register_blueprint(api_postal)

if __name__ == '__main__':

    # create_new_user('test@test.com','123321')
     app.run(host='0.0.0.0',debug=True)