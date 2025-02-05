import requests
from ..core.config import settings


class NotificationService:
    @staticmethod
    def send_notification(title: str, message: str, priority: int = 3) -> None:
        headers = {
            "Title": title,
            "Priority": str(priority),
        }

        if settings.NTFY_ACCESS_TOKEN:
            headers["Authorization"] = f"Bearer {settings.NTFY_ACCESS_TOKEN}"

        response = requests.post(
            settings.NTFY_BASE_URL,
            data=message.encode(encoding="utf-8"),
            headers=headers,
        )
        response.raise_for_status()
