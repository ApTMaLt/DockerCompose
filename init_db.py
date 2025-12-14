import os
import sys
import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from alembic.config import Config
from alembic import command
from app.models import Task
from app.database import SessionLocal, engine

def wait_for_db():
    """Ждём, пока PostgreSQL запустится"""
    while True:
        try:
            conn = engine.connect()
            conn.close()
            break
        except OperationalError:
            print("Waiting for DB...")
            time.sleep(2)

def run_migrations():
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))
    command.upgrade(alembic_cfg, "head")

def seed_data():
    db = SessionLocal()
    if db.query(Task).count() == 0:
        tasks = [
            Task(title="Полить цветы"),
            Task(title="Сделать лабораторную по Docker"),
            Task(title="Выпить кофе ☕")
        ]
        for task in tasks:
            db.add(task)
        db.commit()
        print("Seeded initial data.")
    db.close()

if __name__ == "__main__":
    print("Starting DB initialization...")
    wait_for_db()
    run_migrations()
    seed_data()
    print("DB ready!")