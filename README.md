# Проект: сервис YaCut
[![status](https://github.com/alexpro2022/yacut/actions/workflows/main.yml/badge.svg)](https://github.com/alexpro2022/yacut/actions)
[![codecov](https://codecov.io/gh/alexpro2022/yacut/branch/master/graph/badge.svg?token=PDXTQWRDJ7)](https://codecov.io/gh/alexpro2022/yacut)

На большинстве сайтов адреса страниц довольно длинные. Делиться такими длинными ссылками не всегда удобно, а иногда и вовсе невозможно. Удобнее использовать короткие ссылки. 

Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.



## Оглавление:
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка и запуск](#установка-и-запуск)
- [Автор](#автор)



## Технологии:
<details><summary>Развернуть</summary>

 
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


**Базы данных и инструменты работы с БД:**

[![SQLite3](https://img.shields.io/badge/-SQLite3-464646?logo=SQLite)](https://www.sqlite.com/version3.html)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?logo=sqlalchemy)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?logo=alembic)](https://alembic.sqlalchemy.org/en/latest/)


**Тестирование:**

[![Pytest](https://img.shields.io/badge/-Pytest-464646?logo=Pytest)](https://docs.pytest.org/en/latest/)
[![Pytest-cov](https://img.shields.io/badge/-Pytest--cov-464646?logo=Pytest)](https://pytest-cov.readthedocs.io/en/latest/)
[![Coverage](https://img.shields.io/badge/-Coverage-464646?logo=Python)](https://coverage.readthedocs.io/en/latest/)


**CI/CD:**

[![GitHub_Actions](https://img.shields.io/badge/-GitHub_Actions-464646?logo=GitHub)](https://docs.github.com/en/actions)
[![docker_hub](https://img.shields.io/badge/-Docker_Hub-464646?logo=docker)](https://hub.docker.com/)
[![docker_compose](https://img.shields.io/badge/-Docker%20Compose-464646?logo=docker)](https://docs.docker.com/compose/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?logo=NGINX)](https://nginx.org/ru/)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?logo=Yandex)](https://cloud.yandex.ru/)
[![Telegram](https://img.shields.io/badge/-Telegram-464646?logo=Telegram)](https://core.telegram.org/api)

[⬆️Оглавление](#оглавление)
</details>


## Описание работы:
Ключевые возможности сервиса:
  * генерация коротких ссылок и связь их с исходными длинными ссылками,
  * переадресация на исходный адрес при обращении к коротким ссылкам.

Пользовательский интерфейс сервиса — одна страница с формой. Эта форма состоит из двух полей:
  * обязательного - для длинной исходной ссылки;
  * необязательного - для пользовательского варианта короткой ссылки (не должен превышать 16 символов).

Если пользователь предложит вариант короткой ссылки, который уже занят, то сервис сообщает пользователю об этом уведомлением. При этом, существующая в базе данных ссылка остается неизменной.

Если пользователь не заполнит поле со своим вариантом короткой ссылки, то сервис сгенерирует уникальную ссылку автоматически и добавит ее в базу данных.
Формат для ссылки по умолчанию — шесть случайных символов, в качестве которых можно использовать:
  * большие латинские буквы,
  * маленькие латинские буквы,
  * цифры в диапазоне от 0 до 9.

После отправки формы на главной странице отображается созданная ссылка.

Переход на длинную исходную ссылку осущеставляется по адресу: http://hostname/<имя_короткой_ссылки> , где hostname: 
  * 127.0.0.1:5000 
  * localhost
  * IP-адрес удаленного сервера

в зависимости от способа запуска. Для более подробной информации см. [Установка и запуск](#установка-и-запуск)

Сервис так же предоставляет взаимодействие через API, который доступен всем желающим. Сервис обслуживает два эндпоинта:
  * /api/id/ — POST-запрос на создание новой короткой ссылки;
  * /api/id/<имя_короткой_ссылки>/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

[⬆️Оглавление](#оглавление)



## Установка и запуск:

Удобно использовать copy-paste - команды копировать из GitHub Readme и вставить в командную строку Git Bash или IDE (например VSCode).

### Предварительные условия для Docker Compose:
<details><summary>Развернуть</summary>

Предполагается, что пользователь:
 - создал аккаунт [DockerHub](https://hub.docker.com/), если запуск будет производиться на удаленном сервере.
 - установил [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/) на локальной машине или на удаленном сервере, где проект будет запускаться в контейнерах. Проверить наличие можно выполнив команды:
    ```
    docker --version && docker-compose --version
    ```
</details>
<hr>
<details>
<summary>Локальный запуск</summary> 

1. Клонируйте репозиторий с GitHub и введите данные для переменных окружения (значения даны для примера, но их можно оставить):
```
git clone git@github.com:alexpro2022/yacut-Flask.git && \
cd yacut-Flask && \
cp env_example .env && \
nano .env
```
<details>
<summary>сервер Flask/SQLite3</summary>

2. Создайте и активируйте виртуальное окружение:
   * Если у вас Linux/macOS
   ```
    python -m venv venv && source venv/bin/activate
   ```
   
   * Если у вас Windows
   ```
    python -m venv venv && source venv/Scripts/activate
   ```

3. Установите в виртуальное окружение все необходимые зависимости из файла **requirements.txt**:
```
python -m pip install --upgrade pip && pip install -r requirements.txt
```

4. Создайте БД по сценарию **migrations/** и запустите приложение:
```
flask db upgrade && flask run
```
Сервер Flask запустит приложение по адресу http://127.0.0.1:5000.

5. Остановить приложение можно комбинацией клавиш Ctl-C.
</details>
<details>
<summary>Docker Compose/PostgreSQL</summary>

2. Из корневой директории проекта выполните команду:
```
docker compose -f infra/local/docker-compose.yml up -d --build
```
Проект будет развернут в трех docker-контейнерах (db, web, nginx) по адресу http://localhost.

3. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:
```
docker compose -f infra/local/docker-compose.yml down
```
Если также необходимо удалить тома базы данных и статики:
```
docker compose -f infra/local/docker-compose.yml down -v
```
</details>
<hr></details>

<details>
<summary>Запуск на удаленном сервере</summary>

1. Сделайте [форк](https://docs.github.com/en/get-started/quickstart/fork-a-repo) в свой репозиторий.

2. Создайте Actions.Secrets согласно списку ниже (значения указаны для примера) + переменные окружения из env_example файла:
```
PROJECT_NAME=yacut
SECRET_KEY

POSTGRES_PASSWORD 
DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres

CODECOV_TOKEN 

DOCKERHUB_USERNAME 
DOCKERHUB_PASSWORD 

# Данные удаленного сервера и ssh-подключения:
HOST 
USERNAME 
SSH_KEY     
PASSPHRASE 

# Учетные данные Телеграм-бота для получения сообщения о успешном завершении workflow
TELEGRAM_USER_ID 
TELEGRAM_BOT_TOKEN 
```

3. Запустите вручную workflow, чтобы автоматически развернуть проект в трех docker-контейнерах (db, web, nginx) на удаленном сервере.
</details>
<hr>

[⬆️Оглавление](#оглавление)



## Автор:
[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#Проект-сервис-YaCut)
