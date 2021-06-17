import logging
import sqlite3

from flask import Flask, request, json
from flask import g
from werkzeug.exceptions import HTTPException

DATABASE = 'onlineclass.db'

from model import OnlineLearning

logging.basicConfig(filename='onlineclass.log', level=logging.INFO,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s %(filename)s %(lineno)s: %(message)s')

app = Flask(__name__)


def get_db():
    """
    Create a db instance
    :return:
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.route('/')
def online_class_home():
    return 'Welcome to your Online class!'
    # abort(400)


@app.errorhandler(HTTPException)
def handle_error(e):
    """
    Method to handle error cases
    :param e: error
    :return: Response message
    """
    # response_code = 400
    # response_message = 'Bad request'
    # if isinstance(e, HTTPException):
    #     response_code = e.code
    #     response_message = e.description
    # return jsonify(error=response_message + ' | HTTP response code = ' + str(response_code))

    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


from service.course_service import create_course, edit_course, get_all_courses


@app.route('/course', methods=['GET', 'POST'])
def get_add_courses():
    if request.method == 'GET':
        return get_all_courses()
    elif request.method == 'POST':
        return create_course()


@app.route('/course/<course_id>', methods=['GET', 'PUT', 'DELETE'])
def course_by_id(course_id):
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        return edit_course(course_id)
    elif request.method == 'DELETE':
        pass


@app.route('/subject', methods=['GET', 'POST'])
def subject():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass


@app.route('/tag', methods=['GET', 'POST'])
def tag():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass


@app.route('/video', methods=['POST', 'GET'])
def video():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass


@app.route('/mostviewed', methods=['GET', 'POST'])
def mostviewed():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass


@app.route('/webinar', methods=['GET', 'POST'])
def webinar():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass


@app.route('/suggestion', methods=['GET', 'POST'])
def suggestion():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass


if __name__ == '__main__':
    my_class = OnlineLearning()
    app.run()
