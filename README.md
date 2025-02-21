# Flask User Management API

## Описание
Это простое Flask-приложение для управления пользователями с возможностью их создания, получения и мягкого удаления (soft delete). Приложение использует PostgreSQL в качестве базы данных.

## Установка и запуск

### 1. Запуск базы данных PostgreSQL
Перед запуском приложения убедитесь, что у вас запущен экземпляр PostgreSQL и доступны учетные данные для подключения.

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Настройка переменных окружения

| Переменная       | Описание                                   | Значение по умолчанию |
|------------------|--------------------------------------------|-----------------------|
| POSTGRES_USER    | Имя пользователя БД                        | `user`                |
| POSTGRES_PASSWORD| Пароль пользователя БД                     | ` `                   |
| POSTGRES_HOST    | Хост базы данных                           | `localhost`           |
| POSTGRES_PORT    | Порт для подключения к БД                  | `5432`                |
| POSTGRES_DB      | Название базы данных                       | `db`                  |
| SERVER_PORT      | Порт по которому приложение будет доступно | `8080`                |

### 4. Инициализация базы данных
Таблица user создает автоматически при запуске приложения.

### 5. Запуск приложения
```bash
gunicorn
```
## API Эндпоинты

### 1. Создание пользователя
**POST** `/createuser`
#### Пример запроса:
```sh
curl --location 'http://localhost:8080/api/createuser' \
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
curl -X GET 'http://localhost:8080/api/getuser?name=Alice'
```
#### Ответ:
```json
{"message": "Hello, Alice!"}
```

### 3. Удаление пользователя (soft delete)
**DELETE** `/deleteuser`
#### Пример запроса:
```sh
curl --location --request DELETE 'http://localhost:8080/api/deleteuser' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Alice"
}'
```
#### Ответ:
```json
{"message": "User Alice marked as deleted!"}
```

## Автор
KVOTHE 😊

