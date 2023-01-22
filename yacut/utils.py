import random
from typing import Any

from settings import ALPHABET, CUSTOM_ID_SIZE_AUTO


def get_short_id() -> str:
    return ''.join(random.choice(ALPHABET) for i in range(CUSTOM_ID_SIZE_AUTO))


def get_unique_id(model: Any, field: Any) -> str:
    unique_id = get_short_id()
    while model.query.filter(field == unique_id).count():
        unique_id = get_short_id()
    return unique_id


def is_exist(klass: Any, field: Any, criterion: Any, exception: Any) -> None:
    if klass.query.filter(field == criterion).count():
        raise exception