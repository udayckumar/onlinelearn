from flask import request

from app import db
from model.User import User
from model.UserSchema import UserSchema


def add_user():
    request_payload = request.get_json(force=True)

    if request_payload.keys() >= {'id', 'username', 'is_instructor'}:
        user_id = request_payload['id']
        user_name = request_payload['username']
        first_name = request_payload['first_name'] if ('first_name' in request_payload.keys()) else None
        last_name = request_payload['last_name'] if ('last_name' in request_payload.keys()) else None
        is_instructor = request_payload['is_instructor']

        new_user = User(user_id, user_name, first_name, last_name, is_instructor)

        db.session.add(new_user)
        db.session.commit()

        return UserSchema().jsonify(new_user)


def get_users():
    all_tags = User.query.all()
    result = UserSchema().dumps(all_tags, many=True)
    return result


def update_user(user_id):
    user = User.query.get(user_id)

    user_name = request.json['username']
    user.user_name = user_name
    first_name = request.json['first_name']
    user.first_name = first_name
    last_name = request.json['last_name']
    user.last_name = last_name
    is_instructor = request.json['is_instructor']
    user.is_instructor = is_instructor

    db.session.commit()

    return UserSchema().jsonify(user)


def get_user(user_id):
    user = User.query.get(user_id)
    return UserSchema().dumps(user)


def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return UserSchema().dumps(user)
