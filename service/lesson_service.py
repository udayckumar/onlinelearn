from flask import request

from app import db
from model.Lesson import Lesson
from model.LessonSchema import LessonSchema


def add_lesson():
    lesson_id = request.json['id']
    lesson_name = request.json['name']

    new_lesson = Lesson(lesson_id, lesson_name)

    db.session.add(new_lesson)
    db.session.commit()

    return LessonSchema().jsonify(new_lesson)


def get_lessons():
    all_lessons = Lesson.query.all()
    result = LessonSchema().dumps(all_lessons, many=True)
    return result


def update_lesson(lesson_id):
    lesson = Lesson.query.get(lesson_id)

    lesson_name = request.json['name']
    lesson.lesson_name = lesson_name  # Column name is lesson_name

    db.session.commit()

    return LessonSchema().jsonify(lesson)


def get_lesson(lesson_id):
    lesson = Lesson.query.get(lesson_id)
    return LessonSchema().dumps(lesson)


def delete_lesson(lesson_id):
    lesson = Lesson.query.get(lesson_id)
    db.session.delete(lesson)
    db.session.commit()
    return LessonSchema().dumps(lesson)
