#extensionsdan db connect edirik
from extensions import db
from app import app

class Blog(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(200), nullable = True)

    def __repr__(self):
        return self.title