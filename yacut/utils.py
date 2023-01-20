import random

from .constants import ALPHABET, CUSTOM_ID_SIZE_AUTO
from .error_handlers import InvalidAPIUsage


def get_short_id() -> str:
    return ''.join(random.choice(ALPHABET) for i in range(CUSTOM_ID_SIZE_AUTO))


def get_unique_id(model, field) -> str:
    unique_id = get_short_id()
    while model.query.filter(field == unique_id).count():
        unique_id = get_short_id()
    return unique_id


def create(db, obj):
    db.session.add(obj)
    db.session.commit()


def api_get_or_404(model, field, criterion):
    obj = model.query.filter(field == criterion).first()
    if obj is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return obj
