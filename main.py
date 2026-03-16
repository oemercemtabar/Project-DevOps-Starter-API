from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="DevOps Starter API")

class TaskCreate(BaseModel):
    title: str


tasks = [
    {"id": 1, "title": "Learn DevOps basics", "done": False},
    {"id": 2, "title": "Run FastAPI locally", "done": False},
]

@app.get("/")
def root():
    return {"message": "DevOps Starter API is running!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def list_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
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
    return {"error": "Task not found"}

