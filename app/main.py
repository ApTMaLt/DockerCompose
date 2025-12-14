from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Task

app = FastAPI(title="FastAPI + PostgreSQL Demo")
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def read_tasks(request: Request):
    db: Session = get_db()
    tasks = db.query(Task).all()
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})