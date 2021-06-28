from flask import request

from app import db
from model.Course import Course
from model.CourseSchema import CourseSchema


def add_course():
    course_id = request.json['id']
    course_name = request.json['name']

    new_course = Course(course_id, course_name)

    db.session.add(new_course)
    db.session.commit()

    return CourseSchema().jsonify(new_course)


def get_courses():
    all_courses = Course.query.all()
    result = CourseSchema().dumps(all_courses, many=True)
    return result


def update_course(course_id):
    course = Course.query.get(course_id)

    course_name = request.json['name']
    course.course_name = course_name  # Column name is course_name

    db.session.commit()

    return CourseSchema().jsonify(course)


def get_course(course_id):
    course = Course.query.get(course_id)
    return CourseSchema().dumps(course)


def delete_course(course_id):
    course = Course.query.get(course_id)
    db.session.delete(course)
    db.session.commit()
    return CourseSchema().dumps(course)
