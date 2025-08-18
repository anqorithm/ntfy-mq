FROM python:3.13.7-alpine

WORKDIR /app

# Install poetry and dependencies
RUN pip install --no-cache-dir poetry

# Copy project files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copy application code
COPY . .

# Install the project
RUN poetry install --no-interaction --no-ansi

# Run the application
CMD ["poetry", "run", "fastapi", "run", "notification_service/main.py", "--host", "0.0.0.0", "--port", "8000"] 