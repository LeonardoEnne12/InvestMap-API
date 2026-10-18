# InvestMap-API 🚀

InvestMap-API is a backend API built with **FastAPI** for investment tracking and portfolio management. It enables uploading investment portfolio spreadsheets (Excel `.xlsx`), parsing asset data, analyzing metrics, and persisting statement and position records to the centralized SQLite database.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI** (Web Framework)
- **Uvicorn** (ASGI Server)
- **OpenPyXL** (Spreadsheet Parsing)
- **Pydantic** (Data Validation & Schemas)
- **SQLite3** (Standard Library, SQL-First connection)

---

## 📁 Project Structure

```text
InvestMap-API/
├── app/
│   ├── api/
│   │   ├── __init__.py            # API router aggregation
│   │   └── excel.py               # Excel upload endpoints (POST /upload-excel)
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py              # Application configuration & DATABASE_PATH resolver
│   ├── domain/
│   │   ├── __init__.py            # Domain models export
│   │   ├── db_models.py           # Statement and Position Pydantic models
│   │   └── excel_models.py        # Data models & response schemas
│   ├── parsers/
│   │   ├── __init__.py
│   │   └── excel_parser.py        # Excel parsing logic (openpyxl)
│   ├── repositories/              # SQL-First data persistence layer
│   │   ├── __init__.py            # Repository exports
│   │   ├── database.py            # SQLite connection manager & health checks
│   │   ├── statement_repository.py# Statement CRUD queries
│   │   └── position_repository.py # Position CRUD queries
│   ├── services/
│   │   ├── __init__.py
│   │   └── excel_service.py       # Business logic layer
│   └── main.py                    # FastAPI application entrypoint
├── tests/
│   └── unit/                      # Unit and integration test suite
├── test_app.py                    # Test runner script
├── .env.example                   # Example environment variables
├── requirements.txt               # Dependency requirements
└── README.md                      # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites

Make sure you have **Python 3.10+** installed.

### 2. Create and Activate Virtual Environment

```bash
# Windows (Git Bash)
python -m venv venv
source venv/Scripts/activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup & Configuration

InvestMap-API connects to the SQLite database managed by **InvestMap-DB**. By default, it expects the database at:
```text
../InvestMap-DB/investmap.db
```

To configure a custom database path, copy `.env.example` to `.env` and set `DATABASE_PATH`:
```bash
cp .env.example .env
```

```env
DATABASE_PATH=../InvestMap-DB/investmap.db
```

Make sure the database tables are initialized before running the API:
```bash
# From InvestMap-DB directory
python init_db.py
```

---

## ⚡ Running the API Server

Start the FastAPI server locally using **Uvicorn**:

```bash
uvicorn app.main:app --reload
```

Optionally specify host and port:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

Once running:
- **API Base URL:** `http://127.0.0.1:8000`
- **Swagger Documentation:** `http://127.0.0.1:8000/docs`
- **ReDoc Documentation:** `http://127.0.0.1:8000/redoc`

---

## 🧪 Running Tests

Execute the unit test suite using the test runner:

```bash
python test_app.py
```

Or directly via unittest:

```bash
python -m unittest discover tests/unit
```

---

## 📌 Active API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Root welcome message |
| `GET` | `/health` | System and database connectivity check (`ok` or `degraded`) |
| `POST` | `/upload-excel` | Upload and parse `.xlsx` portfolio spreadsheet |
