from app import db


class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key=True, nullable=False)
    course_name = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
