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