import os


def test_env_vars():
    env_vars = list(os.environ.values())
    if env_vars:
        assert 'sqlite:///db.sqlite3' in env_vars, (
            'Проверьте наличие переменной окружения с настройками для подключения'
            ' базы данных со значением sqlite:///db.sqlite3'
        )


def test_config(default_app):
    assert default_app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///db.sqlite3', (
        'Проверьте, что конфигурационному ключу SQLALCHEMY_DATABASE_URI '
        'присвоено значение с настройками для подключения базы данных'
    )
    assert default_app.config['SECRET_KEY'] == os.getenv('SECRET_KEY', 'qwerty'), (
        'Проверьте, что конфигурационному ключу SECRET_KEY '
        'присвоено значение')
