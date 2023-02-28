# Проект: сервис YaCut.
На большинстве сайтов адреса страниц довольно длинные. Делиться такими длинными ссылками не всегда удобно, а иногда и вовсе невозможно. Удобнее использовать короткие ссылки. 
Например, ссылка ```http://yacut.ru/lesson``` воспринимается лучше, чем ```https://practicum.yandex.ru/trainer/backend-developer/lesson/12e07d96-31f3-449f-abcf-e468b6a39061/```.

Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Оглавление
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка](#установка)
- [Запуск](#запуск)
- [Автор](#автор)


## Технологии
[![Python](https://img.shields.io/pypi/pyversions/sqlalchemy?logo=Python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-Flask-464646?logo=flask)](https://palletsprojects.com/p/flask/)
[![Flask-SQLAlchemy](https://img.shields.io/badge/-FlaskSQLAlchemy-464646?logo=flask)](https://flask-sqlalchemy.palletsprojects.com/en/latest/)
[![Flask-Migrate](https://img.shields.io/badge/-Flask_Migrate-464646?logo=Flask)](https://flask-migrate.readthedocs.io/en/latest/index.html)
[![Flask-WTF](https://img.shields.io/badge/-FlaskWTF-464646?logo=Flask)](https://flask-wtf.readthedocs.io/en/latest/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?logo=sqlalchemy)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?logo=alembic)](https://alembic.sqlalchemy.org/en/latest/)
[![WTForms](https://img.shields.io/badge/-WTForms-464646?logo=wtforms)](https://wtforms.readthedocs.io/en/master/)
[![Jinja](https://img.shields.io/badge/-Jinja-464646?logo=Jinja)](https://palletsprojects.com/p/jinja/)
[![Werkzeug](https://img.shields.io/badge/-Werkzeug-464646?logo=Werkzeug)](https://palletsprojects.com/p/werkzeug/)  

[⬆️Оглавление](#оглавление)



## Описание работы
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

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```

4. Установить все необходимые зависимости из файла **requirements.txt**:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
pip list
```

5. Создать БД по сценарию из репозитория **migrations/**:
```
flask db upgrade
```

[⬆️Оглавление](#оглавление)



## Запуск:

```
(venv) $ flask run
```

[⬆️Оглавление](#оглавление)


## Автор
[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#Проект-парсинга-pep)