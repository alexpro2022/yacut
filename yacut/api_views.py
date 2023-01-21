from http import HTTPStatus

from flask import jsonify, request

from yacut import app, db
from yacut.models import URLMap


@app.route('/api/id/', methods=('POST',))
def api_create():
    return jsonify(
        URLMap().create(db, request.get_json()).to_representation()
    ), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/')
def api_get_link(short_id):
    return jsonify(url=URLMap().get_original_link(short_id)), HTTPStatus.OK
