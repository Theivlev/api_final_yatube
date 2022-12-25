# api_final
"Yatube" - проект социальной сети. 
"API для Yatube" расширяет возможности социальной сети.

Получить, обновить, создать, удалить посты.
Возможность создавать комментарии к постам
Возможность подписываться на посты авторов
JWT Авторизация.

Запуск проекта:

Клонировать репозиторий и перейти в него в командной строке
Создать и активировать виртуальное окружение
python -m venv env
source venv/Scripts/activate
python -m pip install --upgrade pip
Установить зависимости из файла requirements.txt: pip install -r requirements.txt

Выполнить миграции: python manage.py migrate
Запустить проект: python manage.py runserver

Примеры запросов:
POST-запрос с токеном, добавление новой публикации в коллекцию публикаций.
POST http://127.0.0.1:8000/api/v1/posts/
Запрос:
{
"text": "string",
"image": "string",
"group": 0
}

Ответ:
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}

GET-запрос, получение списка доступных сообществ.
GET http://127.0.0.1:8000/api/v1/groups/{id}/
Запрос:
[
{
"id": 0,
"title": "string",
"slug": "string",
"description": "string"
}
]

Ответ:
{
"id": 0,
"title": "string",
"slug": "string",
"description": "string"
}

POST-запрос, Добавление нового комментария к публикации. Анонимные запросы запрещены.
POST http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
Запрос:
{
"text": "string"
}

Ответ:
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}