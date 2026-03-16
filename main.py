from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from settings import settings

app = FastAPI(title=settings.app_name)

class TaskCreate(BaseModel):
    title: str


tasks = [
    {"id": 1, "title": "Learn DevOps basics", "done": False},
    {"id": 2, "title": "Run FastAPI locally", "done": False},
]

@app.get("/")
def root():
    return {
        "message": f"{settings.app_name} is running!",
        "environment": settings.app_env,
        "debug": settings.debug

    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "environment": settings.app_env
    }

@app.get("/tasks")
def list_tasks():
    return {"tasks": tasks}

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": payload.title,
        "done": False
    }
    tasks.append(new_task)
    return new_task

@app.patch("/tasks/{task_id}/done")
def mark_task_done(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

