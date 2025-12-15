from server import db

class Drawing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    img_name = db.Column(db.String(120), nullable=True)
    description = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return str(self.id)