from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, value):
        return check_password_hash(self.password, value)

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.username

class Review(db.Model):
    print 'db.Model : Review'
    __tablename__ = 'Review'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer())
    grade = db.Column(db.Integer())
    comment = db.Column(db.String())

    def __init__(self, user_id, grade, comment):
        self.user_id = user_id
        self.grade = grade
        self.comment = comment

    def __repr__(self):
        return '<Review %r>' % self.grade