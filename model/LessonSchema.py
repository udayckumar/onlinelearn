from flask import app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)


class LessonSchema(ma.Schema):
    class Meta:
        fields = ('lesson_id', 'lesson_name')
