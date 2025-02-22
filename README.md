# Flask User Management API

## Используемые технологии

- **[Docker+docker-compose](https://www.docker.com/)**: Инструменты для контейнеризации приложений.
- **[Python v3.9.21](https://www.python.org/downloads/release/python-3921/)**: Язык программирования Python.
- **[Flask](https://flask.palletsprojects.com/en/stable/)**: Фреймворк для создания микросервисов.
- **[Gunicorn](https://gunicorn.org/)**: HTTP-сервер Python WSGI для UNIX
- **[Nginx](https://nginx.org/ru/)**: обратынй прокси сервер
- **[Certbot](https://github.com/certbot/certbot)**: инструмент для выдачи сектификатов letsencrypt

## Описание
Flask-приложение для управления пользователями с возможностью их создания, получения и мягкого удаления (soft delete). Приложение использует PostgreSQL в качестве базы данных.


## Настройка

Для запуска необходим `.env` файл в корне репозитория.

### Пример `.env` файла

```bash
POSTGRES_HOST=user_db
POSTGRES_PORT=5432
POSTGRES_USER=secret_user
POSTGRES_PASSWORD=secret_passwd
POSTGRES_DB=users
SERVER_PORT=8000
```

### Описание настроек

| Переменная       | Описание                                   | Значение по умолчанию  |
|------------------|--------------------------------------------|------------------------|
| POSTGRES_USER    | Имя пользователя БД                        | `user`                 |
| POSTGRES_PASSWORD| Пароль пользователя БД                     | `super_secret_password`|
| POSTGRES_HOST    | Хост базы данных                           | `localhost`            |
| POSTGRES_PORT    | Порт для подключения к БД                  | `5432`                 |
| POSTGRES_DB      | Название базы данных                       | `db`                   |
| SERVER_PORT      | Порт по которому приложение будет доступно | `8080`                 |


## Запуск приложения

- **Запуск сервисов в фоновом режиме:**

```bash
make up
```

- **Остановка сервиса:**

```bash
make down
```

- **Перезапуск сервисов:**

```bash
make restart
```
Другие команды см. [Makefile](Makefile)

## API Эндпоинты

### 1. Создание пользователя
**POST** `/createuser`
#### Пример запроса:
```sh
curl --location 'http://localhost/api/createuser' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Alice"
}'
```
#### Ответ:
```json
{"message": "User Alice created!"}
```

### 2. Получение пользователя
**GET** `/getuser?name=<name>`
#### Пример запроса:
```sh
curl -X GET 'http://localhost/api/getuser?name=Alice'
```
#### Ответ:
```json
{"message": "Hello, Alice!"}
```

### 3. Удаление пользователя (soft delete)
**DELETE** `/deleteuser`
#### Пример запроса:
```sh
curl --location --request DELETE 'http://localhost/api/deleteuser' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Alice"
}'
```
### 4. Healthcheck
**GET** `/health`
#### Пример запроса:
```sh
curl --location --request GET 'http://localhost/api/health'
```
#### Ответ:
```json
{"message":"Ok"}
```

## Автор
KVOTHE 😊

