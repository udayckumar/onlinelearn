from flask import app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)


class CourseSchema(ma.Schema):
    class Meta:
        fields = ('course_id', 'course_name')
