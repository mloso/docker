# DockerFirstApp

Telegram бот с интеграцией языковых моделей через OpenRouter API.

## Возможности

- 🤖 Асинхронная работа на aiogram
- 🧠 Поддержка различных LLM через OpenRouter
- 🐳 Полная контейнеризация в Docker
- 🔒 Безопасное хранение ключей через переменные окружения

## Установка и запуск

### Локальный запуск

1. Клонируйте репозиторий
2. Установите зависимости: `pip install -r requirements.txt`
3. Создайте `.env` файл с вашими ключами: `mv .env_dist .env`
4. Запустите: `PYTHONPATH=app python bot/main.py`

### Запуск в Docker

```bash
# Сборка образа
docker build -t dockerfirstapp .

# Запуск контейнера
docker run -d \
  --name dockerfirstapp-bot \
  --restart unless-stopped \
  --env-file .env \
  dockerfirstapp
```