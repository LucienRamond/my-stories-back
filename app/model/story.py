from server import db

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    story = db.Column(db.String(10000), nullable=False)

    def __repr__(self):
        return str(self.id)