from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Celery
    CELERY_BROKER_URL: str = "amqp://guest:guest@rabbitmq:5672//"

    # Ntfy
    NTFY_TOPIC: str
    NTFY_ACCESS_TOKEN: str
    NTFY_BASE_URL: str

    # Service Info
    SERVICE_NAME: str = "Notification Service"
    SERVICE_DESCRIPTION: str = "Modern async notification service using ntfy.sh"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    # API Settings
    API_PREFIX: str = "/api/v1"

    class Config:
        env_file = ".env"


settings = Settings()
