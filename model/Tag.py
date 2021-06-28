from app import db


class Tag(db.Model):
    tag_id = db.Column(db.Integer, primary_key=True, nullable=False)
    tag_name = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, tag_id, tag_name):
        self.tag_id = tag_id
        self.tag_name = tag_name
