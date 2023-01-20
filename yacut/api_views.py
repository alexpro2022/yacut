from flask import jsonify, request

from . import app, db
from .models import URLMap
from .utils import get_or_404


@app.route('/api/id/', methods=('POST',))
def api_create():
    return jsonify(
        URLMap().create(db, request.get_json()).to_representation()
    ), 201


@app.route('/api/id/<short_id>/')
def api_get_link(short_id):
    return jsonify(url=get_or_404(URLMap, URLMap.short, short_id).original), 200
