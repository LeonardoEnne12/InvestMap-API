# InvestMap-API Project Context & Memory

> **Note for AI Assistant:** This file registers the ongoing architecture, goals, state, and endpoints of InvestMap-API. Read and update this document whenever major alterations or feature additions occur to optimize token usage and keep repository context concise.

---

## 📌 Project Overview
- **Name:** InvestMap-API
- **Goal:** Backend API for investment portfolio management and tracking. Provides endpoints for statement/position management and analytics, persisting records into the centralized SQLite database.
- **Tech Stack:** Python 3.10+, FastAPI, Uvicorn, Pydantic, SQLite3 (Standard Library).

---

## 🛠️ Architecture & Endpoints

### Application Structure
```
InvestMap-API/
├── app/
│   ├── __init__.py
│   ├── main.py                        # Main FastAPI entrypoint & router configuration
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py                  # App configuration & DATABASE_PATH resolver (.env loader)
│   ├── api/
│   │   └── __init__.py                # API router aggregation & export
│   ├── domain/
│   │   ├── __init__.py                # Domain models export
│   │   └── db_models.py               # Statement and Position Pydantic models
│   ├── parsers/
│   │   └── __init__.py                # Data parsing & ingestion interfaces
│   ├── services/
│   │   └── __init__.py                # Business logic services
│   └── repositories/
│       ├── __init__.py                # Repository exports
│       ├── database.py                # SQLite connection manager, get_db, & check_db_connection
│       ├── statement_repository.py    # SQL-First CRUD queries for statements
│       └── position_repository.py     # SQL-First CRUD queries for positions
├── tests/
│   └── unit/
│       └── test_api.py                # Unit and integration tests for API endpoints
├── .agents/
│   └── AGENTS.md                      # Project context & AI memory (this file)
├── .env.example                       # Example environment variables (DATABASE_PATH)
├── .gitignore                         # Git ignore rules
├── requirements.txt                   # Python dependencies
└── README.md                          # Project documentation
```

### Environment Variables
- `DATABASE_PATH`: Path to the SQLite database file. Defaults to `../InvestMap-DB/investmap.db` (resolved relative to `InvestMap-API`). Can be configured in `.env`.

### Database & Repository Conventions (SQL-First)
- **Integration with InvestMap-DB:** Consumes the SQLite database initialized externally from `InvestMap-DB/schema.sql`.
- **No ORM DDL:** Never execute `CREATE TABLE` or auto-generate schema from Python.
- **Connection Management:** `app.repositories.database.get_db_connection()` context manager ensures:
  - `PRAGMA foreign_keys = ON;` is executed on every connection.
  - `conn.row_factory = sqlite3.Row` for key-based column access.
  - Automatic commit on normal return and rollback on exceptions.
- **Repository Pattern:** Pure parameterized SQL (`?`) statements located in `StatementRepository` and `PositionRepository`, mapping rows into Pydantic models (`Statement`, `Position`).

### Active Endpoints
- `GET /`: Health check / welcome message.
- `GET /health`: System and database connectivity check (returns status `"ok"` or `"degraded"`, and database details).
