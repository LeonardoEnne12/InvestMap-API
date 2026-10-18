import sqlite3
from typing import Optional, List
from app.domain.db_models import Position, PositionCreate
from app.repositories.database import get_db_connection


class PositionRepository:
    """
    Repository for CRUD operations on the 'positions' table.
    Follows SQL-First pattern with pure parameterized SQL queries.
    """

    @staticmethod
    def create(position_in: PositionCreate, conn: Optional[sqlite3.Connection] = None) -> Position:
        sql = """
            INSERT INTO positions (id, statement_id, ticker, category, quantity, price, currency)
            VALUES (?, ?, ?, ?, ?, ?, ?);
        """
        params = (
            position_in.id,
            position_in.statement_id,
            position_in.ticker,
            position_in.category,
            position_in.quantity,
            position_in.price,
            position_in.currency,
        )

        def _execute(c: sqlite3.Connection) -> Position:
            cursor = c.cursor()
            cursor.execute(sql, params)
            cursor.execute(
                "SELECT id, statement_id, ticker, category, quantity, price, currency FROM positions WHERE id = ?;",
                (position_in.id,)
            )
            row = cursor.fetchone()
            return Position(**dict(row))

        if conn is not None:
            return _execute(conn)
        with get_db_connection() as c:
            return _execute(c)

    @staticmethod
    def create_many(positions_in: List[PositionCreate], conn: Optional[sqlite3.Connection] = None) -> List[Position]:
        if not positions_in:
            return []

        sql = """
            INSERT INTO positions (id, statement_id, ticker, category, quantity, price, currency)
            VALUES (?, ?, ?, ?, ?, ?, ?);
        """
        params_list = [
            (
                p.id,
                p.statement_id,
                p.ticker,
                p.category,
                p.quantity,
                p.price,
                p.currency,
            )
            for p in positions_in
        ]

        def _execute(c: sqlite3.Connection) -> List[Position]:
            cursor = c.cursor()
            cursor.executemany(sql, params_list)
            # Retrieve inserted positions
            ids = [p.id for p in positions_in]
            placeholders = ",".join("?" for _ in ids)
            cursor.execute(
                f"SELECT id, statement_id, ticker, category, quantity, price, currency FROM positions WHERE id IN ({placeholders});",
                ids
            )
            rows = cursor.fetchall()
            return [Position(**dict(row)) for row in rows]

        if conn is not None:
            return _execute(conn)
        with get_db_connection() as c:
            return _execute(c)

    @staticmethod
    def get_by_id(position_id: str, conn: Optional[sqlite3.Connection] = None) -> Optional[Position]:
        sql = """
            SELECT id, statement_id, ticker, category, quantity, price, currency
            FROM positions
            WHERE id = ?;
        """

        def _execute(c: sqlite3.Connection) -> Optional[Position]:
            cursor = c.cursor()
            cursor.execute(sql, (position_id,))
            row = cursor.fetchone()
            return Position(**dict(row)) if row else None

        if conn is not None:
            return _execute(conn)
        with get_db_connection() as c:
            return _execute(c)

    @staticmethod
    def get_by_statement_id(statement_id: str, conn: Optional[sqlite3.Connection] = None) -> List[Position]:
        sql = """
            SELECT id, statement_id, ticker, category, quantity, price, currency
            FROM positions
            WHERE statement_id = ?
            ORDER BY ticker ASC;
        """

        def _execute(c: sqlite3.Connection) -> List[Position]:
            cursor = c.cursor()
            cursor.execute(sql, (statement_id,))
            rows = cursor.fetchall()
            return [Position(**dict(row)) for row in rows]

        if conn is not None:
            return _execute(conn)
        with get_db_connection() as c:
            return _execute(c)

    @staticmethod
    def get_by_ticker(ticker: str, conn: Optional[sqlite3.Connection] = None) -> List[Position]:
        sql = """
            SELECT id, statement_id, ticker, category, quantity, price, currency
            FROM positions
            WHERE ticker = ?;
        """

        def _execute(c: sqlite3.Connection) -> List[Position]:
            cursor = c.cursor()
            cursor.execute(sql, (ticker,))
            rows = cursor.fetchall()
            return [Position(**dict(row)) for row in rows]

        if conn is not None:
            return _execute(conn)
        with get_db_connection() as c:
            return _execute(c)

    @staticmethod
    def delete_by_statement_id(statement_id: str, conn: Optional[sqlite3.Connection] = None) -> int:
        sql = "DELETE FROM positions WHERE statement_id = ?;"

        def _execute(c: sqlite3.Connection) -> int:
            cursor = c.cursor()
            cursor.execute(sql, (statement_id,))
            return cursor.rowcount

        if conn is not None:
            return _execute(conn)
        with get_db_connection() as c:
            return _execute(c)
