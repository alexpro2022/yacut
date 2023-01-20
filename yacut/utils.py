import random

from werkzeug.exceptions import NotFound

from .constants import ALPHABET, CUSTOM_ID_SIZE_AUTO
from .error_handlers import InvalidAPIUsage


def get_short_id() -> str:
    return ''.join(random.choice(ALPHABET) for i in range(CUSTOM_ID_SIZE_AUTO))


def get_unique_id(model, field) -> str:
    unique_id = get_short_id()
    while model.query.filter(field == unique_id).count():
        unique_id = get_short_id()
    return unique_id


def get_or_404(model, field, criterion, api=True):
    try:
        obj = model.query.filter(field == criterion).first_or_404()
    except NotFound:
        if api:
            raise InvalidAPIUsage('Указанный id не найден', 404)
        raise NotFound
    return obj
