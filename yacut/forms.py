import re

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import InputRequired, Length, URL, ValidationError

from .constants import CUSTOM_ID_SIZE_MANUAL, LINK_SIZE_MAX, LINK_SIZE_MIN
from .models import URLMap


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
        # Здесь Regexp не работает, так как это поле может быть пустым
        # Regexp(r'[a-zA-Z0-9]*', message='Не соотвествует шаблону.'),
    ])
    submit = SubmitField('Создать')

    def validate_custom_id(form, field) -> None:
        if not field.data:
            return

        invalid_symbols = set(re.sub(r'[a-zA-Z0-9]+', '', field.data))
        if invalid_symbols:
            raise ValidationError(
                f'Неверные символы {invalid_symbols} в идентификаторе: "{field.data}"')

        if URLMap.query.filter_by(short=field.data).count():
            raise ValidationError(f'Имя {field.data} уже занято!')
