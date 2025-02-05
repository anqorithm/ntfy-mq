# Ntfy MQ 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95.0+-green.svg)](https://fastapi.tiangolo.com)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)](https://www.docker.com/)

Simple notification service that uses ntfy.sh to send notifications through RabbitMQ and Celery.

## Tech Stack

- **Python**: Core programming language
- **FastAPI**: High-performance web framework for building APIs
- **RabbitMQ**: Message broker for handling notification queue
- **Celery**: Distributed task queue for processing notifications
- **Poetry**: Dependency management and packaging
- **ntfy.sh**: Push notification service
- **Docker**: Containerization

## Features

- Asynchronous notification processing
- Scalable architecture using message queues
- RESTful API endpoints for sending notifications
- Easy integration with existing systems
- Support for multiple notification types
- Docker support for easy deployment

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Poetry (for local development)

### Using Docker

1. Clone the repository:
```bash
git clone https://github.com/anqol/ntfy-mq.git
cd ntfy-mq
```

2. Build and run with Docker Compose:
```bash
docker-compose up --build
```

### Local Development

1. Install dependencies:
```bash
poetry install
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Start RabbitMQ server
4. Start Celery worker:
```bash
poetry run celery -A app.worker worker --loglevel=info
```

5. Start FastAPI server:
```bash
poetry run fastapi dev notification_service/main.py
```

## API Endpoints

### Send Notification
- **POST** `/api/v1/notify`
- Creates a new notification
- Request body:
```json
{
    "title": "string",
    "message": "string",
    "priority": "low|normal|high"
}
```

### Check Task Status
- **GET** `/api/v1/tasks/{task_id}`
- Returns the status of a notification task

### Health Check
- **GET** `/api/v1/health`
- Returns detailed service health status including:
  - Service name and version
  - System uptime and memory usage
  - Response time metrics
  - Environment details
  - Dependencies status
  - API documentation links
Example response:
```json
{
    "service": "Ntfy MQ",
    "description": "Notification service using ntfy.sh, RabbitMQ, and Celery",
    "version": "1.0.0",
    "status": "healthy",
    "timestamp": "2024-01-20T12:34:56.789Z",
    "uptime": "2d 3h 45m",
    "memory_usage": {
        "total": "1.2GB",
        "used": "756MB",
        "free": "444MB"
    },
    "response_time": "42ms",
    "environment": "production",
    "dependencies": {
        "rabbitmq": "healthy",
        "celery": "healthy",
        "ntfy": "healthy"
    },
    "host": {
        "ip": "192.168.1.100",
        "hostname": "ntfy-mq-server"
    },
    "documentation": {
        "swagger": "http://localhost:8000/docs",
        "redoc": "http://localhost:8000/redoc",
        "github": "https://github.com/anqorithm/ntfy-mq"
    }
}
```

## Documentation

API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contributors

- [Abdullah Alqahtani](https://github.com/anqorithm)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```