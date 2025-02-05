from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Celery
    CELERY_BROKER_URL: str = "amqp://guest:guest@rabbitmq:5672//"

    # Ntfy
    NTFY_TOPIC: str
    NTFY_ACCESS_TOKEN: str
    NTFY_BASE_URL: str = "https://ntfy.sh"

    # Service Info
    SERVICE_NAME: str = "Ntfy MQ Service"
    SERVICE_DESCRIPTION: str = (
        "Ntfy MQ is a modern async notification service using ntfy.sh through RabbitMQ and Celery"
    )
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    # API Settings
    API_PREFIX: str = "/api/v1"

    class Config:
        env_file = ".env"


settings = Settings()
