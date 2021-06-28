from app import db


class Video(db.Model):
    video_id = db.Column(db.Integer, primary_key=True, nullable=False)
    video_title = db.Column(db.String(150), unique=True, nullable=False)
    video_link = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, video_id, video_title, video_link):
        self.video_id = video_id
        self.video_title = video_title
        self.video_link = video_link
