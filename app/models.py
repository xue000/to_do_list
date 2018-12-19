from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self,password):
        return check_password_hash(self.password_hash, password)

class Task (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), index=True)
    description = db.Column(db.String(250), index=True)
    date = db.Column(db.Date)
    status = db.Column(db.String(15),index=True,default="Uncompleted")
    # represent the task
    def __repr__(self):
        return  self.title
