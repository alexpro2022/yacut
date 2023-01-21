import re
from datetime import datetime as dt
from typing import Dict, Tuple

from flask_sqlalchemy import SQLAlchemy

from settings import (
    API_ORIGINAL_REQUEST, API_ORIGINAL_RESPONSE,
    API_SHORT_REQUEST, API_SHORT_RESPONSE,
    BASE_URL, CUSTOM_ID_SIZE_MANUAL,
    FORM_ORIGINAL, FORM_SHORT, LINK_SIZE_MAX, REGEXP,
)
from yacut import db
from yacut.exceptions import InvalidAPIUsage
from yacut.utils import get_unique_id


class TimestampMixin:
    timestamp = db.Column(db.DateTime, default=dt.utcnow)


class PKModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)


class URLMap(TimestampMixin, PKModel):
    original = db.Column(
        db.String(LINK_SIZE_MAX),
        nullable=False,
    )
    short = db.Column(
        db.String(CUSTOM_ID_SIZE_MANUAL),
        unique=True,
        nullable=False,
        index=True,
    )

    def __repr__(self) -> str:
        return (
            f'id: {self.id}\n'
            f'original: {self.original}\n'
            f'short: {self.short}\n'
            f'timestamp: {self.timestamp}\n'
        )

    @classmethod
    def get_original_link(cls, short_id: str, api: bool = True) -> str:
        return cls.query.filter_by(short=short_id).first_or_404(api).original

    @classmethod
    def __clean_data(cls, data: Dict[str, str], post: bool = False) -> Tuple[str, str]:
        if not data:
            raise InvalidAPIUsage('Отсутствует тело запроса')
        original = data.get(API_ORIGINAL_REQUEST)
        short = data.get(API_SHORT_REQUEST)
        if post and not original:
            raise InvalidAPIUsage(f'"{API_ORIGINAL_REQUEST}" является обязательным полем!')
        if not short:
            short = get_unique_id(cls, cls.short)
        elif len(short) > CUSTOM_ID_SIZE_MANUAL or re.sub(REGEXP, '', short):
            raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
        elif cls.query.filter_by(short=short).count():
            raise InvalidAPIUsage(f'Имя "{short}" уже занято.')
        return original, short

    def to_intenal_value(self, data: Dict[str, str], clean: bool = True, post: bool = False):
        if clean:
            self.original, self.short = self.__class__.__clean_data(data, post)
        else:
            self.original = data[FORM_ORIGINAL]
            self.short = data[FORM_SHORT]
        return self

    def create(self, db: SQLAlchemy, data: Dict[str, str], validation: bool = True):
        db.session.add(self.to_intenal_value(data, clean=validation, post=True))
        db.session.commit()
        return self

    def to_representation(self) -> Dict[str, str]:
        return {
            API_ORIGINAL_RESPONSE: self.original,
            API_SHORT_RESPONSE: (BASE_URL + self.short),
        }