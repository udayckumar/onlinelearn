from flask import app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)


class SubjectSchema(ma.Schema):
    class Meta:
        fields = ('subject_id', 'subject_name')
