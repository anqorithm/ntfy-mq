# Ntfy MQ 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.8+-green.svg)](https://fastapi.tiangolo.com)
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
    "priority": 1  // Priority level from 1-5
}
```

#### Priority Levels
| Priority Level | Value | Description | Behavior |
|---------------|-------|-------------|-----------|
| Max/Urgent | 5 | Highest priority notifications | Really long vibration bursts, default notification sound with pop-over |
| High | 4 | Important notifications | Long vibration burst, default notification sound with pop-over |
| Default | 3 | Standard notifications | Short default vibration and sound, default notification behavior |
| Low | 2 | Non-urgent notifications | No vibration or sound, only visible when notification drawer is pulled down |
| Min | 1 | Minimal priority | No vibration or sound, shown under "Other notifications" |

### Check Task Status
- **GET** `/api/v1/tasks/{task_id}`
- Returns the status of a notification task

### Health Check
- **GET** `/health`
- Returns service health status
- Example response:
```json
{
    "service": "Notification Service",
    "description": "Modern async notification service using ntfy.sh",
    "status": "healthy",
    "version": "1.0.0",
    "timestamp": "2025-02-05T09:30:23.962722Z",
    "environment": "development"
}
```

### Root Endpoint
- **GET** `/`
- Returns service information and available endpoints
- Example response:
```json
{
    "name": "Notification Service",
    "description": "Modern async notification service using ntfy.sh",
    "version": "1.0.0",
    "endpoints": {
        "root": "/",
        "health": "/health", 
        "docs": "/docs",
        "redoc": "/redoc",
        "openapi": "/openapi.json",
        "api_v1": "/api/v1"
    },
    "timestamp": "2025-02-05T09:30:33.522773Z"
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

## References

- [ntfy.sh](https://ntfy.sh)
- [RabbitMQ](https://www.rabbitmq.com)
- [Celery](https://docs.celeryq.dev)
- [FastAPI](https://fastapi.tiangolo.com)
