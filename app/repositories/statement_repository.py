import sqlite3
from typing import Optional, List
from app.domain.db_models import Statement, StatementCreate
from app.repositories.database import get_db_connection


class StatementRepository:
    """
    Repository for CRUD operations on the 'statements' table.
    Follows SQL-First pattern with pure parameterized SQL queries.
    """

    @staticmethod
    def create(statement_in: StatementCreate, conn: Optional[sqlite3.Connection] = None) -> Statement:
        sql = """
            INSERT INTO statements (id, source, reference_date, currency, total_net_worth)
            VALUES (?, ?, ?, ?, ?);
        """
        params = (
            statement_in.id,
            statement_in.source,
            statement_in.reference_date,
            statement_in.currency,
            statement_in.total_net_worth,
        )

        def _execute(c: sqlite3.Connection) -> Statement:
            cursor = c.cursor()
            cursor.execute(sql, params)
            cursor.execute(
                "SELECT id, source, reference_date, currency, total_net_worth, created_at FROM statements WHERE id = ?;",
                (statement_in.id,)
            )
            row = cursor.fetchone()
            return Statement(**dict(row))

        if conn is not None:
            return _execute(conn)
        with get_db_connection() as c:
            return _execute(c)

    @staticmethod
    def get_by_id(statement_id: str, conn: Optional[sqlite3.Connection] = None) -> Optional[Statement]:
        sql = """
            SELECT id, source, reference_date, currency, total_net_worth, created_at
            FROM statements
            WHERE id = ?;
        """

        def _execute(c: sqlite3.Connection) -> Optional[Statement]:
            cursor = c.cursor()
            cursor.execute(sql, (statement_id,))
            row = cursor.fetchone()
            return Statement(**dict(row)) if row else None

        if conn is not None:
            return _execute(conn)
        with get_db_connection() as c:
            return _execute(c)

    @staticmethod
    def list_all(limit: int = 100, offset: int = 0, conn: Optional[sqlite3.Connection] = None) -> List[Statement]:
        sql = """
            SELECT id, source, reference_date, currency, total_net_worth, created_at
            FROM statements
            ORDER BY created_at DESC
            LIMIT ? OFFSET ?;
        """

        def _execute(c: sqlite3.Connection) -> List[Statement]:
            cursor = c.cursor()
            cursor.execute(sql, (limit, offset))
            rows = cursor.fetchall()
            return [Statement(**dict(row)) for row in rows]

        if conn is not None:
            return _execute(conn)
        with get_db_connection() as c:
            return _execute(c)

    @staticmethod
    def delete(statement_id: str, conn: Optional[sqlite3.Connection] = None) -> bool:
        sql = "DELETE FROM statements WHERE id = ?;"

        def _execute(c: sqlite3.Connection) -> bool:
            cursor = c.cursor()
            cursor.execute(sql, (statement_id,))
            return cursor.rowcount > 0

        if conn is not None:
            return _execute(conn)
        with get_db_connection() as c:
            return _execute(c)
