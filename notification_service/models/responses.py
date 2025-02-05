from pydantic import BaseModel


class NotificationResponse(BaseModel):
    status: str
    message: str
