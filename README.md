# FastAPI (FastAPIUsers, PostgreSQL, SQLAlchemy, Alembic, Pydantic)

## О проекте
- Моя первая настройка RestAPI приложения через FastAPI
- Данные передаются через ORM-запросы к базе данных PostgreSQL
- ORM-запросы реализованы через SQLAlchemy
- Добавлены роутеры на регистрацию, логин и выход (FastAPIUsers)
- Добавлены роутеры на проверку авторизации (Через статус внутри FastAPIusers current_user())
- Добавлены роутеры на работу с вводимыми данными
- Добавлен Alembic для создания ревизий и возможности создания миграций (отслеживания изменения структуры бд)
- Аутентификация через Cookie + JWT-токен

## Что я на данный момент учу
- Внедрение GUI Flet через Flet-FastAPI
- Добавление pytest к роутерам

## Установка
```sh
git clone https://github.com/Broys42/FastAPI.git
cd FastAPI
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn src.main:app --reload
```

## Структура проекта
```sh
│   .env
│   .gitignore
│   alembic.ini
│   requirements.txt
│   README.md
│
├───migrations
│   │   env.py
│   │   README
│   │   script.py.mako
│   │
│
├───src
│   │   config.py
│   │   database.py
│   │   main.py
│   │   orm.py
│   │
│   ├───auth
│   │   │   auth.py
│   │   │   manager.py
│   │   │   schemas.py
│   │   │
```

## .env
```sh
DB_HOST: str
DB_PORT: int
DB_USER: str
DB_PASS: str
DB_NAME: str
CREATE_TABLES: bool
```

## Скриншоты
[![Screenshot-9.jpg](https://i.postimg.cc/Zq5bn2H0/Screenshot-9.jpg)](https://postimg.cc/RW25bPjz)
[![Screenshot-8.jpg](https://i.postimg.cc/sf62WVqy/Screenshot-8.jpg)](https://postimg.cc/s1WydR30)
