from typing import Any

from flask_sqlalchemy import BaseQuery
from werkzeug.exceptions import NotFound

from yacut.exceptions import InvalidAPIUsage


class MyQuery(BaseQuery):
    def first_or_404(self, api: bool = False) -> Any:
        try:
            obj = super().first_or_404()
        except NotFound:
            if api:
                raise InvalidAPIUsage('Указанный id не найден', 404)
            raise NotFound
        return obj