from flask import request

from app import db
from model.Subject import Subject
from model.SubjectSchema import SubjectSchema


def add_subject():
    subject_id = request.json['id']
    subject_name = request.json['name']

    new_subject = Subject(subject_id, subject_name)

    db.session.add(new_subject)
    db.session.commit()

    return SubjectSchema().jsonify(new_subject)


def get_subjects():
    all_subjects = Subject.query.all()
    result = SubjectSchema().dumps(all_subjects, many=True)
    return result


def update_subject(subject_id):
    subject = Subject.query.get(subject_id)

    subject_name = request.json['name']
    subject.subject_name = subject_name  # Column name is subject_name

    db.session.commit()

    return SubjectSchema().jsonify(subject)


def get_subject(subject_id):
    subject = Subject.query.get(subject_id)
    return SubjectSchema().dumps(subject)


def delete_subject(subject_id):
    subject = Subject.query.get(subject_id)
    db.session.delete(subject)
    db.session.commit()
    return SubjectSchema().dumps(subject)
