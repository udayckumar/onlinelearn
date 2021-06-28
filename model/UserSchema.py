from flask import app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'user_name', 'first_name', 'last_name', 'is_instructor')
