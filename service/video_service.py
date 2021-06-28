from flask import request

from app import db
from model.Video import Video
from model.VideoSchema import VideoSchema


def add_video():
    video_id = request.json['id']
    video_title = request.json['title']
    video_url = request.json['link']

    new_video = Video(video_id, video_title, video_url)

    db.session.add(new_video)
    db.session.commit()

    return VideoSchema().jsonify(new_video)


def get_videoes():
    all_videoes = Video.query.all()
    result = VideoSchema().dumps(all_videoes, many=True)
    return result


def update_video(video_id):
    video = Video.query.get(video_id)

    video_title = request.json['title']
    video.video_title = video_title  # Column name is video_title

    video_url = request.json['link']
    video.video_link = video_url  # Column name is video_url

    db.session.commit()

    return VideoSchema().jsonify(video)


def get_video(video_id):
    video = Video.query.get(video_id)
    return VideoSchema().dumps(video)


def delete_video(video_id):
    video = Video.query.get(video_id)
    db.session.delete(video)
    db.session.commit()
    return VideoSchema().dumps(video)
