# 1. Базовый образ с Python
FROM python:3.11-slim

# 2. Устанавливаем зависимости системы, нужные Poetry и сборке пакетов
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential gcc \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 3. Устанавливаем Poetry
ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# 4. Отключаем создание виртуального окружения внутри poetry (используем системное)
ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'

# 5. Устанавливаем рабочую директорию
WORKDIR /app

# 6. Копируем файлы зависимостей
COPY pyproject.toml poetry.lock ./

# 7. Устанавливаем зависимости
RUN poetry install --no-root --no-interaction

# 8. Копируем весь проект
COPY . .

# 9. Указываем команду запуска
CMD ["poetry", "run", "python", "main.py"]