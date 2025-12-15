import os
from model.drawing import Drawing
from flask import send_file
from pathlib import Path
from server import app, db

class DrawingsService():
    def get_all_drawings():
        drawings = (Drawing.query.all())

        return [{
            "id":drawing.id,
            "name":drawing.name,
            "img_name":drawing.img_name,
            "description":drawing.description,
        } for drawing in drawings]

    def get_img_by_name(img_name):
        img = Path(f'imgs/{img_name}')
        return send_file(img)

    def upload_img_file(img, img_name, img_id):
        img.save(os.path.join(app.config['UPLOAD_FOLDER'], img_name))
        drawing = Drawing.query.filter_by(id=img_id).first()
        drawing.img_name = img_name

        db.session.commit()

        return 'Image bien enregistrée !'

    def upload_img_data(img_data):
        drawing = Drawing(name=img_data["name"], description=img_data['description'])
        db.session.add(drawing)
        db.session.commit()

        return (f'{drawing.id}')

    def delete_drawing(drawing_id):
        drawing = Drawing.query.filter_by(id=drawing_id).first()

        os.remove(f'app/imgs/{drawing.img_name}')

        db.session.delete(drawing)
        db.session.commit()

        return (f'Drawing successfully deleted')
