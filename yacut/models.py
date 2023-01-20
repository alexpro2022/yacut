import re
from datetime import datetime as dt

from . import db
from .constants import BASE_URL, CUSTOM_ID_SIZE_MANUAL
from .error_handlers import InvalidAPIUsage
from .utils import create, get_unique_id


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=dt.utcnow)

    def __repr__(self):
        return (
            f'id: {self.id}\n'
            f'original: {self.original}\n'
            f'short: {self.short}\n'
            f'timestamp: {self.timestamp}\n'
        )

    def to_representation(self) -> dict:
        return dict(
            url=self.original,
            short_link=BASE_URL + self.short,
        )

    def clean_data(self, data: dict, post: bool = False):
        if not data:
            raise InvalidAPIUsage('Отсутствует тело запроса')
        original = data.get('url', '')
        short = data.get('custom_id', '')
        if post and not original:
            raise InvalidAPIUsage('"url" является обязательным полем!')
        if not short:
            short = get_unique_id(self.__class__, self.__class__.short)
        elif len(short) > CUSTOM_ID_SIZE_MANUAL:
            raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
        elif re.sub(r'[a-zA-Z0-9]+', '', short):
            raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
        elif self.__class__.query.filter_by(short=short).count():
            raise InvalidAPIUsage(f'Имя "{short}" уже занято.')
        return original, short

    def to_intenal_value(self, data: dict, post: bool = False):
        self.original, self.short = self.clean_data(data, post)
        return self

    def create(self, db, data):
        create(db, self.to_intenal_value(data, True))
        return self