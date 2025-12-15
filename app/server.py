from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from logging import FileHandler,WARNING

UPLOAD_FOLDER = './imgs/'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////home/ubuntu/my-stories-back/instance/database.db"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROPAGATE_EXCEPTIONS'] = True
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)


db = SQLAlchemy(app)

CORS(app, intercept_exceptions=True, supports_credentials=True)

from model.drawing import Drawing
from model.story import Story

from api.drawings import drawings_route
app.register_blueprint(drawings_route)

from api.stories import stories_route
app.register_blueprint(stories_route)

if __name__ == "__name__":
        app.run()

# with app.app_context():
#     db.create_all()
