from http import HTTPStatus
from typing import Literal

from flask import jsonify, request, Response

from yacut import app, db
from yacut.models import URLMap


@app.route('/api/id/', methods=('POST',))
def api_create() -> tuple[Response, Literal[HTTPStatus.CREATED]]:
    return jsonify(
        URLMap().create(db, request.get_json()).to_representation()
    ), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/')
def api_get_link(short_id: str) -> tuple[Response, Literal[HTTPStatus.OK]]:
    return jsonify(url=URLMap.get_original_link(short_id)), HTTPStatus.OK
