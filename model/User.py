from app import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_name = db.Column(db.String(15), unique=True, nullable=False)
    first_name = db.Column(db.String(25), unique=False, nullable=True)
    last_name = db.Column(db.String(25), unique=False, nullable=True)
    is_instructor = db.Column(db.Boolean, unique=False, nullable=False)

    def __init__(self, user_id, user_name, first_name, last_name, is_instructor):
        self.user_id = user_id
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.is_instructor = is_instructor
