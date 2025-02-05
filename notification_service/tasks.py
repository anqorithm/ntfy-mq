import requests
from celery import Celery
from .core.config import settings
from .models import NotificationResponse

celery_app = Celery(
    "notification_service",
    broker=settings.CELERY_BROKER_URL,
    backend="rpc://",
)

celery_app.conf.update(
    task_ignore_result=False,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
)


@celery_app.task(bind=True, max_retries=3)
def send_notification(self, title: str, message: str, priority: int = 3):
    try:
        response = requests.post(
            settings.NTFY_BASE_URL,
            data=message.encode(encoding="utf-8"),
            headers={
                "Title": title,
                "Priority": str(priority),
                "Authorization": f"Bearer {settings.NTFY_ACCESS_TOKEN}",
            },
        )
        response.raise_for_status()
        return NotificationResponse(
            status="success", message="Notification sent successfully"
        )
    except requests.RequestException as e:
        retry_in = 2**self.request.retries
        raise self.retry(exc=e, countdown=retry_in)
