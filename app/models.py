from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

from app import db, login

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'User: {self.username}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def hash_password(self,password):
        return generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password, password)
    
    def get_id(self):
        return str(self.user_id)
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(250))
    card_name = db.Column(db.String(50))
    card_series = db.Column(db.String(50))
    card_number = db.Column(db.String(50))
    card_value = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __repr__(self):
        return f'Post {self.body}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

class Commission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    email = db.Column(db.String(50))
    subject = db.Column(db.String(50))
    request = db.Column(db.String(250))
    budget = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __repr__(self):
        return f'Post {self.body}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()