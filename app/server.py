import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from logging import FileHandler,WARNING
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DEPLOY_DATABASE_URI")
app.config['UPLOAD_FOLDER'] = os.environ.get("UPLOAD_FOLDER")
app.config['PROPAGATE_EXCEPTIONS'] = True
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)


db = SQLAlchemy(app)

CORS(app, intercept_exceptions=True, supports_credentials=True)

from model.drawing import Drawing
from model.story import Story
from model.user import User
from model.message import Message

from api.drawings import drawings_route
app.register_blueprint(drawings_route)

from api.stories import stories_route
app.register_blueprint(stories_route)

from api.user import user_route
app.register_blueprint(user_route)

from api.messages import messages_route
app.register_blueprint(messages_route)

with app.app_context():
    db.create_all()

if __name__ == "__name__":
        app.run()
