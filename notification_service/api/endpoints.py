from fastapi import APIRouter, HTTPException
from .schemas import (
    NotificationRequest,
    NotificationResponse,
    TaskStatusResponse,
    SuccessResponse,
)
from ..tasks.worker import celery_app, send_notification

router = APIRouter()


@router.post("/notify/", response_model=NotificationResponse)
async def create_notification(notification: NotificationRequest):
    try:
        task = send_notification.delay(
            title=notification.title,
            message=notification.message,
            priority=notification.priority,
        )
        return NotificationResponse(
            message="Notification queued successfully",
            task_id=task.id,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/tasks/{task_id}", response_model=TaskStatusResponse)
async def get_task_status(task_id: str):
    try:
        task = celery_app.AsyncResult(task_id)
        response = TaskStatusResponse(
            task_id=task_id,
            status=task.status,
            result=None,
            error=None,
        )

        if task.status == "SUCCESS":
            response.result = task.get()
        elif task.status == "FAILURE":
            response.error = str(task.result)

        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
