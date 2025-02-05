from celery import Celery
from ..core.config import settings
from ..services.notifications import NotificationService
from ..models import NotificationResponse

celery_app = Celery(
    "notification_service",
    broker=settings.CELERY_BROKER_URL,
    backend="rpc://",
)

# Celery Configuration
celery_app.conf.update(
    task_ignore_result=False,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
)


@celery_app.task(
    bind=True,
    max_retries=3,
)
def send_notification(self, title: str, message: str, priority: int = 3):
    try:
        NotificationService.send_notification(title, message, priority)
        response = NotificationResponse(
            status="success", message="Notification sent successfully"
        )
        return response.model_dump()
    except Exception as e:
        retry_in = 2**self.request.retries
        raise self.retry(exc=e, countdown=retry_in)
