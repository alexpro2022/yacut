import random
import re
from typing import Any

from yacut.settings import ALPHABET, CUSTOM_ID_SIZE_AUTO


def get_short_id() -> str:
    return ''.join(random.choice(ALPHABET) for i in range(CUSTOM_ID_SIZE_AUTO))


def get_unique_id(model: Any, field: Any) -> str:
    unique_id = get_short_id()
    while model.query.filter(field == unique_id).count():
        unique_id = get_short_id()
    return unique_id


def is_exist(class_: Any, field: Any, criterion: Any, exception: Exception) -> None:
    if class_.query.filter(field == criterion).count():
        raise exception


def get_invalid_symbols(pattern: str, string: str):
    return set(re.sub(pattern, '', string))