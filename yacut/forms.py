from typing import Any

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, InputRequired, Length, ValidationError

from yacut.models import URLMap
from yacut.settings import (CUSTOM_ID_SIZE_MANUAL, LINK_SIZE_MAX,
                            LINK_SIZE_MIN, a_zA_Z0_9)
from yacut.utils import get_invalid_symbols, is_exist


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
            invalid_symbols = get_invalid_symbols(a_zA_Z0_9, field.data)
            if invalid_symbols:
                raise ValidationError(
                    f'Неверные символы {invalid_symbols} в идентификаторе: "{field.data}"')
            is_exist(URLMap, URLMap.short, field.data, ValidationError(f'Имя {field.data} уже занято!'))
