from flask import Blueprint, request
from app.services.drawings_service import DrawingsService
from werkzeug.utils import secure_filename
import os

drawings_route = Blueprint("drawings_route", __name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@drawings_route.route('/drawings', methods=['GET'])
def get_drawings():
    return DrawingsService.get_all_drawings()

@drawings_route.route('/drawings/<string:img_name>', methods=['GET'])
def get_img(img_name):
    return DrawingsService.get_img_by_name(img_name)

@drawings_route.route('/drawings/delete/<int:drawing_id>', methods=['DELETE'])
def delete_drawing(drawing_id):
    return DrawingsService.delete_drawing(drawing_id)

@drawings_route.route('/drawings/upload-img-file/<int:drawing_id>', methods=['POST'])
def post_img_file(drawing_id):
    file = request.files["file"]
    if allowed_file(file.filename):
        img_name = secure_filename(file.filename)
        name, extension = os.path.splitext(img_name)
        return DrawingsService.upload_img_file(file, (f'{str(drawing_id)}{extension}'), drawing_id)        

@drawings_route.route('/drawings/upload-img-data', methods=['POST'])
def post_img_data():
    data = request.get_json()
    return DrawingsService.upload_img_data(data)
