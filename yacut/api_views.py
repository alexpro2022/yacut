from flask import jsonify, request

from . import app, db
from .models import URLMap
from .utils import api_get_or_404


@app.route('/api/id/', methods=('POST',))
def api_create():
    # url_map = URLMap().create(db, request.get_json())
    return jsonify(
        # url_map.to_representation()
        URLMap().create(db, request.get_json()).to_representation()
    ), 201


@app.route('/api/id/<short_id>/')
def api_get_link(short_id):
    return jsonify(url=api_get_or_404(URLMap, URLMap.short, short_id).original), 200
