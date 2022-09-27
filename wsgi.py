from app import app
from api_postal import api_postal

app.register_blueprint(api_postal)
