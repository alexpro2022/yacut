import os

from yacut.settings import DEFAULT_DATABASE, DEFAULT_SECRET_KEY


def _test_env_vars():
    env_vars = list(os.environ.values())
    if env_vars:
        assert DEFAULT_DATABASE in env_vars, (
            f'Проверьте наличие переменной окружения с настройками для подключения'
            f' базы данных со значением {DEFAULT_DATABASE}'
        )


def test_config(default_app):
    assert default_app.config['SQLALCHEMY_DATABASE_URI'] == DEFAULT_DATABASE, (
        'Проверьте, что конфигурационному ключу SQLALCHEMY_DATABASE_URI '
        'присвоено значение с настройками для подключения базы данных'
    )
    assert default_app.config['SECRET_KEY'] == os.getenv('SECRET_KEY', DEFAULT_SECRET_KEY), (
        'Проверьте, что конфигурационному ключу SECRET_KEY '
        'присвоено значение')
