import re
from typing import Any

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import InputRequired, Length, URL, ValidationError

from settings import CUSTOM_ID_SIZE_MANUAL, LINK_SIZE_MAX, LINK_SIZE_MIN, REGEXP
from yacut.models import URLMap
from yacut.utils import is_exist


class MyForm(FlaskForm):
    original_link = URLField('*Длинная ссылка', [
        InputRequired('Обязательное поле.'),
        Length(
            LINK_SIZE_MIN, LINK_SIZE_MAX,
            'Длина ссылки должна быть  %(min)d - %(max)d символов.'),
        URL(message='Неверный формат адреса ссылки.'),
    ])
    custom_id = StringField('Введите идентификатор', [
        Length(
            max=CUSTOM_ID_SIZE_MANUAL,
            message='Идентификатор не может быть длиннее %(max)d символов.'),
    ])
    submit = SubmitField('Создать')

    def validate_custom_id(form: Any, field: Any) -> None:
        if field.data:
            invalid_symbols = set(re.sub(REGEXP, '', field.data))
            if invalid_symbols:
                raise ValidationError(
                    f'Неверные символы {invalid_symbols} в идентификаторе: "{field.data}"')
            is_exist(URLMap, URLMap.short, field.data, ValidationError(f'Имя {field.data} уже занято!'))
