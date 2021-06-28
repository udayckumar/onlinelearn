from flask import request

from app import db
from model.Tag import Tag
from model.TagSchema import TagSchema


def add_tag():
    tag_id = request.json['id']
    tag_name = request.json['name']

    new_tag = Tag(tag_id, tag_name)

    db.session.add(new_tag)
    db.session.commit()

    return TagSchema().jsonify(new_tag)


def get_tags():
    all_tags = Tag.query.all()
    result = TagSchema().dumps(all_tags, many=True)
    return result


def update_tag(tag_id):
    tag = Tag.query.get(tag_id)

    tag_name = request.json['name']
    tag.tag_name = tag_name  # Column name is tag_name

    db.session.commit()

    return TagSchema().jsonify(tag)


def get_tag(tag_id):
    tag = Tag.query.get(tag_id)
    return TagSchema().dumps(tag)


def delete_tag(tag_id):
    tag = Tag.query.get(tag_id)
    db.session.delete(tag)
    db.session.commit()
    return TagSchema().dumps(tag)
