import re
from datetime import datetime as dt

from . import db
from .constants import (
    API_ORIGINAL_REQUEST, API_ORIGINAL_RESPONSE,
    API_SHORT_REQUEST, API_SHORT_RESPONSE,
    BASE_URL, CUSTOM_ID_SIZE_MANUAL,
    FORM_ORIGINAL, FORM_SHORT,
)
from .error_handlers import InvalidAPIUsage
from .utils import get_unique_id


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(CUSTOM_ID_SIZE_MANUAL), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=dt.utcnow)

    def __repr__(self):
        return (
            f'id: {self.id}\n'
            f'original: {self.original}\n'
            f'short: {self.short}\n'
            f'timestamp: {self.timestamp}\n'
        )

    def to_representation(self) -> dict:
        return {
            API_ORIGINAL_RESPONSE: self.original,
            API_SHORT_RESPONSE: (BASE_URL + self.short),
        }

    def clean_data(self, data: dict, post: bool = False):
        if not data:
            raise InvalidAPIUsage('Отсутствует тело запроса')
        original = data.get(API_ORIGINAL_REQUEST, '')
        short = data.get(API_SHORT_REQUEST, '')
        if post and not original:
            raise InvalidAPIUsage(f'"{API_ORIGINAL_REQUEST}" является обязательным полем!')
        if not short:
            short = get_unique_id(self.__class__, self.__class__.short)
        elif len(short) > CUSTOM_ID_SIZE_MANUAL or re.sub(r'[a-zA-Z0-9]+', '', short):
            raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
        # elif re.sub(r'[a-zA-Z0-9]+', '', short):
        #    raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
        elif self.__class__.query.filter_by(short=short).count():
            raise InvalidAPIUsage(f'Имя "{short}" уже занято.')
        return original, short

    def to_intenal_value(self, data: dict, clean=True, post: bool = False):
        if clean:
            self.original, self.short = self.clean_data(data, post)
        else:
            self.original = data[FORM_ORIGINAL]
            self.short = data[FORM_SHORT]
        return self

    def create(self, db, data, validation=True):
        db.session.add(self.to_intenal_value(data, clean=validation, post=True))
        db.session.commit()
        return self