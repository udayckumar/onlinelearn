import json
import logging
import os

from flask import Flask, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

logging.basicConfig(filename='onlineclass.log', level=logging.INFO,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s %(filename)s %(lineno)s: %(message)s')

# Initialize app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# DB Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'resources/onlineclass_db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

from model.TagSchema import TagSchema

# Init schema
tag_schema = TagSchema()
tags_schema = TagSchema(many=True)


@app.errorhandler(HTTPException)
def handle_error(e):
    """
    Method to handle error cases
    :param e: error
    :return: Response message
    """
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


from service import tag_service, subject_service, user_service


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return user_service.get_users()
    elif request.method == 'POST':
        return user_service.add_user()


@app.route('/user/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def user(user_id):
    if request.method == 'GET':
        return user_service.get_user(user_id)
    elif request.method == 'PUT':
        return user_service.update_user(user_id)
    elif request.method == 'DELETE':
        return user_service.delete_user(user_id)


@app.route('/tags', methods=['GET', 'POST'])
def tags():
    if request.method == 'GET':
        return tag_service.get_tags()
    elif request.method == 'POST':
        return tag_service.add_tag()


@app.route('/tag/<tag_id>', methods=['GET', 'PUT', 'DELETE'])
def tag(tag_id):
    if request.method == 'GET':
        return tag_service.get_tag(tag_id)
    elif request.method == 'PUT':
        return tag_service.update_tag(tag_id)
    elif request.method == 'DELETE':
        return tag_service.delete_tag(tag_id)


@app.route('/subjects', methods=['GET', 'POST'])
def subjects():
    if request.method == 'GET':
        return subject_service.get_subjects()
    elif request.method == 'POST':
        return subject_service.add_subject()


@app.route('/subject/<subject_id>', methods=['GET', 'PUT', 'DELETE'])
def subject(subject_id):
    if request.method == 'GET':
        return subject_service.get_subject(subject_id)
    elif request.method == 'PUT':
        return subject_service.update_subject(subject_id)
    elif request.method == 'DELETE':
        return subject_service.delete_subject(subject_id)


from service import course_service


@app.route('/courses', methods=['GET', 'POST'])
def courses():
    if request.method == 'GET':
        return course_service.get_courses()
    elif request.method == 'POST':
        return course_service.add_course()


@app.route('/course/<course_id>', methods=['GET', 'PUT', 'DELETE'])
def course(course_id=None):
    if request.method == 'GET':
        return course_service.get_course(course_id)
    elif request.method == 'PUT':
        return course_service.update_course(course_id)
    elif request.method == 'DELETE':
        return course_service.delete_course(course_id)


@app.route('/lessons', methods=['GET', 'POST'])
def lessons():
    if request.method == 'GET':
        return lesson_service.get_lessons()
    elif request.method == 'POST':
        return lesson_service.add_lesson()


@app.route('/lesson/<lesson_id>', methods=['GET', 'PUT', 'DELETE'])
def lesson(lesson_id=None):
    if request.method == 'GET':
        return lesson_service.get_lesson(lesson_id)
    elif request.method == 'PUT':
        return lesson_service.update_lesson(lesson_id)
    elif request.method == 'DELETE':
        return lesson_service.delete_lesson(lesson_id)


from service import video_service


@app.route('/videoes', methods=['GET', 'POST'])
def videos():
    if request.method == 'GET':
        return video_service.get_videoes()
    elif request.method == 'POST':
        return video_service.add_video()


@app.route('/video/<video_id>', methods=['GET', 'PUT', 'DELETE'])
def video(video_id=None):
    if request.method == 'GET':
        return video_service.get_video(video_id)
    elif request.method == 'PUT':
        return video_service.update_video(video_id)
    elif request.method == 'DELETE':
        return video_service.delete_video(video_id)


if __name__ == '__main__':
    # my_class = OnlineLearning()
    app.run()
