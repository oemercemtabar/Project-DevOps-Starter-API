from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from settings import settings

engine = create_engine(settings.database_url, future=True)


def check_database_connection() -> dict:
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1")).scalar()
            return {
                "ok": True,
                "result": result,
            }
    except SQLAlchemyError as exc:
        return {
            "ok": False,
            "error": str(exc),
        }


def initialize_database() -> None:
    create_table_query = text(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT FALSE
        )
        """
    )

    with engine.begin() as connection:
        connection.execute(create_table_query)


def get_all_tasks() -> list[dict]:
    query = text(
        """
        SELECT id, title, done
        FROM tasks
        ORDER BY id
        """
    )

    with engine.connect() as connection:
        rows = connection.execute(query).mappings().all()
        return [dict(row) for row in rows]


def create_task_in_db(title: str) -> dict:
    query = text(
        """
        INSERT INTO tasks (title, done)
        VALUES (:title, FALSE)
        RETURNING id, title, done
        """
    )

    with engine.begin() as connection:
        row = connection.execute(query, {"title": title}).mappings().first()
        return dict(row)


def mark_task_done_in_db(task_id: int) -> dict | None:
    query = text(
        """
        UPDATE tasks
        SET done = TRUE
        WHERE id = :task_id
        RETURNING id, title, done
        """
    )

    with engine.begin() as connection:
        row = connection.execute(query, {"task_id": task_id}).mappings().first()
        return dict(row) if row else None