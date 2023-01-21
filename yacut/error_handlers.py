from http import HTTPStatus
from typing import Dict, Literal, Tuple

from flask import render_template, jsonify, Response

from yacut import app, db
from yacut.exceptions import InvalidAPIUsage


class InvalidAPIUsage(Exception):
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, msg, status_code=None) -> None:
        super().__init__()
        self.msg = msg
        if status_code is not None:
            self.status_code = status_code

    def to_representation(self) -> Dict[str, str]:
        return dict(message=self.msg)


@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(error) -> Tuple[str, Literal[HTTPStatus.NOT_FOUND]]:
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_error(error) -> Tuple[str, Literal[HTTPStatus.INTERNAL_SERVER_ERROR]]:
    db.session.rollback()
    return render_template('500.html'), HTTPStatus.INTERNAL_SERVER_ERROR


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error) -> tuple[Response, int]:
    return jsonify(error.to_representation()), error.status_code
