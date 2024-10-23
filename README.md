# backend

## API Endpoints

### FavoriteEvents

- **Создание нового `FavoriteEvents`**:

  ```bash
  curl -X POST http://127.0.0.1:8000/api/favorite-events/ -H "Content-Type: application/json" -d '{"user_id": 1, "event_id": 2}'
  ```

- **Получение всех `FavoriteEvents`**:

  ```bash
  curl http://127.0.0.1:8000/api/favorite-events/
  ```

- **Обновление `FavoriteEvents`**:

  ```bash
  curl -X PUT http://127.0.0.1:8000/api/favorite-events/1/ -H "Content-Type: application/json" -d '{"user_id": 1, "event_id": 3}'
  ```

- **Удаление `FavoriteEvents`**:

  ```bash
  curl -X DELETE http://127.0.0.1:8000/api/favorite-events/1/
  ```

### ViewedEvents

- **Создание нового `ViewedEvents`**:

  ```bash
  curl -X POST http://127.0.0.1:8000/api/viewed-events/ -H "Content-Type: application/json" -d '{"user_id": 1, "event_id": 2}'
  ```

- **Получение всех `ViewedEvents`**:

  ```bash
  curl http://127.0.0.1:8000/api/viewed-events/
  ```

- **Обновление `ViewedEvents`**:

  ```bash
  curl -X PUT http://127.0.0.1:8000/api/viewed-events/1/ -H "Content-Type: application/json" -d '{"user_id": 1, "event_id": 3}'
  ```

- **Удаление `ViewedEvents`**:

  ```bash
  curl -X DELETE http://127.0.0.1:8000/api/viewed-events/1/
  ```

## Структура проекта

- **favorites/models.py**: Определение моделей `FavoriteEvents` и `ViewedEvents`.
- **favorites/serializers.py**: Сериализаторы для моделей.
- **favorites/views.py**: ViewSets для CRUD операций.
- **favorites/urls.py**: URL-маршруты для API.
- **back/urls.py**: Подключение URL-адресов приложения к проекту.