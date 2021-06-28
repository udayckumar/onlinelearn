from flask import app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class TagSchema(ma.Schema):
    class Meta:
        fields = ('tag_id', 'tag_name')
