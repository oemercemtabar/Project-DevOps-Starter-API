import logging

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from db import (
    check_database_connection,
    create_task_in_db,
    get_all_tasks,
    initialize_database,
    mark_task_done_in_db,
)
from settings import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.app_name)


class TaskCreate(BaseModel):
    title: str


@app.on_event("startup")
def on_startup():
    logger.info("Initializing database")
    initialize_database()


@app.get("/")
def root():
    logger.info("Root endpoint accessed")
    return {
        "message": f"{settings.app_name} is running!",
        "environment": settings.app_env,
        "debug": settings.debug,
        "database_url": settings.database_url,
    }


@app.get("/health")
def health():
    logger.info("Health check endpoint accessed")
    return {
        "status": "ok",
        "environment": settings.app_env,
    }


@app.get("/health/db")
def health_db():
    logger.info("Database health check endpoint accessed")
    db_status = check_database_connection()

    if not db_status["ok"]:
        logger.warning("Database health check failed: %s", db_status["error"])
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=db_status["error"],
        )

    return {
        "status": "ok",
        "database": db_status,
    }


@app.get("/tasks")
def list_tasks():
    logger.info("List tasks endpoint accessed")
    return {"tasks": get_all_tasks()}


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate):
    logger.info("Create task endpoint accessed with title: %s", payload.title)
    return create_task_in_db(payload.title)


@app.patch("/tasks/{task_id}/done")
def mark_task_done(task_id: int):
    logger.info("Mark task done endpoint accessed for task_id: %d", task_id)
    task = mark_task_done_in_db(task_id)

    if task is None:
        logger.warning("Task not found for task_id: %d", task_id)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    return task