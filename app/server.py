from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

UPLOAD_FOLDER = 'app/imgs/'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)

CORS(app, supports_credentials=True)

from app.model.drawing import Drawing
from app.model.story import Story

from app.api.drawings import drawings_route
app.register_blueprint(drawings_route)

from app.api.stories import stories_route
app.register_blueprint(stories_route)

# with app.app_context():
#     db.create_all()
