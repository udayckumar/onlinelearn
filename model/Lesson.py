from app import db


class Lesson(db.Model):
    lesson_id = db.Column(db.Integer, primary_key=True, nullable=False)
    lesson_name = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, lesson_id, lesson_name):
        self.lesson_id = lesson_id
        self.lesson_name = lesson_name
