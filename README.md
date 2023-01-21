# Проект: сервис YaCut.

## Оглавление
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка](#установка)
- [Запуск](#запуск)
- [Автор](#автор)


## Технологии
  - Создание веб-приложений - Flask;
  - Работа с реляционными БД - SQLAlchemy (Flask-SQLAchemy, Flask-Migrate);
  - Создание HTML-шаблонов - Jinja2;
  - Работа с HTML-формами - WTForms (Flask-WTF);
  - API - реализован кастомный интерфейс на базе модели URLMap и классе исключений InvalidApiUsage.

[⬆️Оглавление](#оглавление)



## Описание работы
На большинстве сайтов адреса страниц довольно длинные. Запоминать и делиться такими длинными ссылками не всегда удобно, а иногда и вовсе невозможно. Удобнее использовать короткие ссылки. Например, ссылки http://yacut.ru/lesson и http://yacut.ru/12e07d воспринимаются лучше, чем https://practicum.yandex.ru/trainer/backend-developer/lesson/12e07d96-31f3-449f-abcf-e468b6a39061/.
Проект YaCut — это сервис укорачивания ссылок.
Его назначение:
 - ассоциировать (сохранить в БД) длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис;
 - переадресация на исходный адрес при обращении к коротким ссылкам.

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