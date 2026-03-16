import logging

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from settings import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.app_name)

class TaskCreate(BaseModel):
    title: str


tasks = [
    {"id": 1, "title": "Learn DevOps basics", "done": False},
    {"id": 2, "title": "Run FastAPI locally", "done": False},
]

@app.get("/")
def root():
    logger.info("Root endpoint accessed inside Docker build practice")
    return {
        "message": f"{settings.app_name} is running!",
        "environment": settings.app_env,
        "debug": settings.debug

    }

@app.get("/health")
def health():
    logger.info("Health check endpoint accessed")
    return {
        "status": "ok",
        "environment": settings.app_env
    }

@app.get("/tasks")
def list_tasks():
    logger.info("List tasks endpoint accessed")
    return {"tasks": tasks}

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate):
    logger.info("Create task endpoint accessed with title: %s", payload.title)
    new_task = {
        "id": len(tasks) + 1,
        "title": payload.title,
        "done": False
    }
    tasks.append(new_task)
    return new_task

@app.patch("/tasks/{task_id}/done")
def mark_task_done(task_id: int):
    logger.info("Marking task %d as done", task_id)
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    logger.warning("Task not found for task_id: %d", task_id)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

