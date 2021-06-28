from app import db


class Subject(db.Model):
    subject_id = db.Column(db.Integer, primary_key=True, nullable=False)
    subject_name = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, subject_id, subject_name):
        self.subject_id = subject_id
        self.subject_name = subject_name

    # @property
    # def courses(self):
    #     return self._courses
    #
    # @courses.setter
    # def subjects(self, courses):
    #     self._courses = courses
