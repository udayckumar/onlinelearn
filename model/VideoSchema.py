from flask import app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)


class VideoSchema(ma.Schema):
    class Meta:
        fields = ('video_id', 'video_title', 'video_link')
