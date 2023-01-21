import random
from typing import Any

from werkzeug.exceptions import NotFound

from settings import ALPHABET, CUSTOM_ID_SIZE_AUTO
from yacut.error_handlers import InvalidAPIUsage


def get_short_id() -> str:
    return ''.join(random.choice(ALPHABET) for i in range(CUSTOM_ID_SIZE_AUTO))


def get_unique_id(model: Any, field: Any) -> str:
    unique_id = get_short_id()
    while model.query.filter(field == unique_id).count():
        unique_id = get_short_id()
    return unique_id


def get_or_404(model: Any, field: Any, criterion: Any, api=True) -> Any:
    try:
        obj = model.query.filter(field == criterion).first_or_404()
    except NotFound:
        if api:
            raise InvalidAPIUsage('Указанный id не найден', 404)
        raise NotFound
    return obj
