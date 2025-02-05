from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class NotificationRequest(BaseModel):
    """Notification request schema"""

    title: str
    message: str
    priority: int = Field(default=3, ge=1, le=5, description="Priority level (1-5)")
    topic: str = Field(..., description="ntfy.sh topic to send the notification to")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "Test Notification",
                "message": "This is a test notification",
                "priority": 3,
                "topic": "test",
            }
        }
    )


class NotificationResponse(BaseModel):
    """Notification response schema"""

    message: str
    task_id: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "message": "Notification queued successfully",
                "task_id": "123e4567-e89b-12d3-a456-426614174000",
            }
        }
    )


class TaskStatusResponse(BaseModel):
    """Task status response schema"""

    task_id: str
    status: str = Field(
        description="Task status: PENDING, STARTED, SUCCESS, FAILURE, RETRY, REVOKED"
    )
    result: dict | None = None
    error: str | None = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "task_id": "123e4567-e89b-12d3-a456-426614174000",
                "status": "SUCCESS",
                "result": {
                    "status": "success",
                    "message": "Notification sent successfully",
                },
                "error": None,
            }
        }
    )


class SuccessResponse(BaseModel):
    """Success response schema"""

    status: str = Field(default="success")
    message: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "status": "success",
                "message": "Operation completed successfully",
            }
        }
    )


class HealthResponse(BaseModel):
    """Health check response schema"""

    service: str
    description: str
    status: str = "healthy"
    version: str
    timestamp: datetime
    environment: str | None = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service": "Notification Service",
                "description": "Modern async notification service using ntfy.sh",
                "status": "healthy",
                "version": "1.0.0",
                "timestamp": "2024-03-14T12:00:00.000Z",
                "environment": "development",
            }
        }
    )


class RootResponse(BaseModel):
    """Root endpoint response schema"""

    name: str
    description: str
    version: str
    endpoints: dict[str, str]
    timestamp: datetime
    user_agent: str | None = None
    ip_address: str | None = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Notification Service",
                "description": "Modern async notification service using ntfy.sh",
                "version": "1.0.0",
                "endpoints": {
                    "root": "/",
                    "health": "/health",
                    "docs": "/docs",
                    "redoc": "/redoc",
                    "openapi": "/openapi.json",
                    "api_v1": "/api/v1",
                },
                "timestamp": "2024-03-14T12:00:00.000Z",
                "user_agent": "Mozilla/5.0",
                "ip_address": "127.0.0.1",
            }
        }
    )
