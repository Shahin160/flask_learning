#extensionsdan db connect edirik
from extensions import db
from app import app

# Flask Model dersi
# class Blog(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     title = db.Column(db.String(200), nullable = True)

#     def __repr__(self):
#         return self.title

# Flask WTF

class contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    services = db.Column(db.String(3))
    budget = db.Column(db.Integer)
    message = db.Column(db.Text, nullable=False)



    def __repr__(self):
        return self.full_name
        
    def __init__(self, full_name, email, services, budget, message):
        self.full_name = full_name
        self.email = email
        self.services = services
        self.budget = budget
        self.message = message


    def save(self):
        db.session.add(self)
        db.session.commit()

# flask db migrate

# flask db upgrade