import sqlite3
from contextlib import contextmanager
from typing import Generator, Dict, Any, List
from app.core.config import settings


@contextmanager
def get_db_connection() -> Generator[sqlite3.Connection, None, None]:
    """
    Context manager providing a managed SQLite connection.
    - Enables foreign key constraints (PRAGMA foreign_keys = ON).
    - Sets row_factory to sqlite3.Row for column name-based access.
    - Automatically commits on success and rolls back on exception.
    """
    conn = sqlite3.connect(settings.database_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")

    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def get_db() -> Generator[sqlite3.Connection, None, None]:
    """
    FastAPI dependency yielding an active SQLite database connection.
    """
    with get_db_connection() as conn:
        yield conn


def check_db_connection() -> Dict[str, Any]:
    """
    Verifies SQLite database connectivity and schema readiness.
    Used for health checks and diagnostics.
    """
    db_file_exists = settings.database_path.is_file()

    if not db_file_exists:
        return {
            "connected": False,
            "database_path": str(settings.database_path),
            "file_exists": False,
            "tables": [],
            "error": f"Database file does not exist at {settings.database_path}. Run init_db.py in InvestMap-DB."
        }

    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1;")

            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name;"
            )
            tables: List[str] = [row[0] for row in cursor.fetchall()]

            return {
                "connected": True,
                "database_path": str(settings.database_path),
                "file_exists": True,
                "tables": tables,
                "error": None
            }
    except Exception as exc:
        return {
            "connected": False,
            "database_path": str(settings.database_path),
            "file_exists": db_file_exists,
            "tables": [],
            "error": str(exc)
        }
