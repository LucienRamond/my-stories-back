from server import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    avatar_img = db.Column(db.String(255), nullable=True)
    password_hash = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"User(name={self.username})"