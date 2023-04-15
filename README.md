# Проект: сервис YaCut
[![status](https://github.com/alexpro2022/yacut/actions/workflows/main.yml/badge.svg)](https://github.com/alexpro2022/yacut/actions)
[![codecov](https://codecov.io/gh/alexpro2022/yacut/branch/master/graph/badge.svg?token=PDXTQWRDJ7)](https://codecov.io/gh/alexpro2022/yacut)

На большинстве сайтов адреса страниц довольно длинные. Делиться такими длинными ссылками не всегда удобно, а иногда и вовсе невозможно. Удобнее использовать короткие ссылки. 
Например, ссылка ```http://yacut.ru/lesson``` воспринимается лучше, чем ```https://practicum.yandex.ru/trainer/backend-developer/lesson/12e07d96-31f3-449f-abcf-e468b6a39061/```.

Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.



## Оглавление:
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка](#установка)
- [Запуск](#запуск)
- [Автор](#автор)



## Технологии:

**Языки программирования и модули:**

[![Python](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue?logo=python)](https://www.python.org/)
[![datetime](https://img.shields.io/badge/-datetime-464646?logo=Python)](https://docs.python.org/3/library/datetime.html)
[![http](https://img.shields.io/badge/-http-464646?logo=Python)](https://docs.python.org/3/library/http.html)
[![os](https://img.shields.io/badge/-os-464646?logo=python)](https://docs.python.org/3/library/os.html)
[![random](https://img.shields.io/badge/-random-464646?logo=Python)](https://docs.python.org/3/library/random.html)
[![re](https://img.shields.io/badge/-re-464646?logo=Python)](https://docs.python.org/3/library/re.html)
[![string](https://img.shields.io/badge/-string-464646?logo=python)](https://docs.python.org/3/library/string.html)
[![typing](https://img.shields.io/badge/-typing-464646?logo=Python)](https://docs.python.org/3/library/typing.html)

[![HTML](https://img.shields.io/badge/-HTML-464646?logo=HTML)](https://html.spec.whatwg.org/multipage/)


**Фреймворк, расширения и библиотеки:**

[![Flask](https://img.shields.io/badge/-Flask-464646?logo=flask)](https://palletsprojects.com/p/flask/)
[![Flask-Migrate](https://img.shields.io/badge/-Flask_Migrate-464646?logo=Flask)](https://flask-migrate.readthedocs.io/en/latest/index.html)
[![Flask-SQLAlchemy](https://img.shields.io/badge/-FlaskSQLAlchemy-464646?logo=flask)](https://flask-sqlalchemy.palletsprojects.com/en/latest/)
[![Flask-WTF](https://img.shields.io/badge/-FlaskWTF-464646?logo=Flask)](https://flask-wtf.readthedocs.io/en/latest/)
[![Jinja](https://img.shields.io/badge/-Jinja-464646?logo=Jinja)](https://palletsprojects.com/p/jinja/)
[![Werkzeug](https://img.shields.io/badge/-Werkzeug-464646?logo=Werkzeug)](https://palletsprojects.com/p/werkzeug/)
[![WTForms](https://img.shields.io/badge/-WTForms-464646?logo=wtforms)](https://wtforms.readthedocs.io/en/master/)


**База данных:**

[![SQLite3](https://img.shields.io/badge/-SQLite3-464646?logo=SQLite)](https://www.sqlite.com/version3.html)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?logo=sqlalchemy)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?logo=alembic)](https://alembic.sqlalchemy.org/en/latest/)


**Тесты:**

[![Pytest](https://img.shields.io/badge/-Pytest-464646?logo=Pytest)](https://docs.pytest.org/en/latest/)
[![Pytest-cov](https://img.shields.io/badge/-Pytest--cov-464646?logo=Pytest)](https://pytest-cov.readthedocs.io/en/latest/)
[![Coverage](https://img.shields.io/badge/-Coverage-464646?logo=Python)](https://coverage.readthedocs.io/en/latest/)


**CI/CD:**

[![GitHub](https://img.shields.io/badge/-GitHub-464646?logo=GitHub)](https://docs.github.com/en)
[![GitHub_Actions](https://img.shields.io/badge/-GitHub_Actions-464646?logo=GitHub)](https://docs.github.com/en/actions)
[![Telegram](https://img.shields.io/badge/-Telegram-464646?logo=Telegram)](https://core.telegram.org/api)



[⬆️Оглавление](#оглавление)



## Описание работы:
Ключевые возможности сервиса:
  * генерация коротких ссылок и связь их с исходными длинными ссылками,
  * переадресация на исходный адрес при обращении к коротким ссылкам.

Пользовательский интерфейс сервиса — одна страница с формой. Эта форма состоит из двух полей:
  * обязательного - для длинной исходной ссылки;
  * необязательного-  для пользовательского варианта короткой ссылки (не должен превышать 16 символов).

Если пользователь предложит вариант короткой ссылки, который уже занят, то сервис сообщает пользователю об этом уведомлением. При этом, существующая в базе данных ссылка остается неизменной.

Если пользователь не заполнит поле со своим вариантом короткой ссылки, то сервис сгенерирует уникальную ссылку автоматически и добавит ее в базу данных.
Формат для ссылки по умолчанию — шесть случайных символов, в качестве которых можно использовать:
  * большие латинские буквы,
  * маленькие латинские буквы,
  * цифры в диапазоне от 0 до 9.

После отправки формы на главной странице отображается созданная ссылка.

Переход на длинную исходную ссылку осущеставляется при вводе в адресную строку браузера:
	<hostname>/<имя_короткой_ссылки>

Сервис так же предоставляет взаимодействие через API, который доступен всем желающим. Сервис обслуживает два эндпоинта:
  - /api/id/ — POST-запрос на создание новой короткой ссылки;
  - /api/id/<имя_короткой_ссылки>/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

[⬆️Оглавление](#оглавление)



## Установка:
1. Клонировать репозиторий с GitHub:
```
git clone git@github.com:alexpro2022/yacut.git
```

2. Перейти в созданную директорию проекта:
```
cd yacut
```

3. Создать и активировать виртуальное окружение:
```
python -m venv venv
```
* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас Windows

    ```
    source venv/Scripts/activate
    ```

4. Установить все необходимые зависимости из файла **requirements.txt**:
```
python -m pip install --upgrade pip && pip install -r requirements.txt && pip list
```

5. Скопируйте содержимое файла **env_example** (при этом будет создан файл *.env*):
```
cp env_example .env
```

6. Откройте новый **.env**-файл и введите данные для переменных окружения.

7. Создать БД по сценарию из репозитория **migrations/**:
```
flask db upgrade
```

[⬆️Оглавление](#оглавление)



## Запуск:

```
flask run
```

[⬆️Оглавление](#оглавление)



## Автор:
[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#Проект-сервис-YaCut)
