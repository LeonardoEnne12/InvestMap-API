# InvestMap-API 🚀

InvestMap-API is a backend API built with **FastAPI** for investment tracking and portfolio management. It enables uploading investment portfolio spreadsheets (Excel `.xlsx`), parsing asset data, and analyzing metrics.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI** (Web Framework)
- **Uvicorn** (ASGI Server)
- **OpenPyXL** (Spreadsheet Parsing)
- **Pydantic** (Data Validation & Schemas)

---

## 📁 Project Structure

```text
InvestMap-API/
├── app/
│   ├── api/
│   │   ├── __init__.py        # API router aggregation
│   │   └── excel.py           # Excel upload endpoints (POST /upload-excel)
│   ├── domain/
│   │   └── excel_models.py    # Data models & response schemas
│   ├── parsers/
│   │   └── excel_parser.py    # Excel parsing logic (openpyxl)
│   ├── repositories/          # Data persistence layer
│   ├── services/
│   │   └── excel_service.py   # Business logic layer
│   └── main.py                # FastAPI application entrypoint
├── tests/
│   └── unit/                  # Unit and integration test suite
├── test_app.py                # Test runner script
├── requirements.txt           # Dependency requirements
└── README.md                  # Project documentation
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
| `GET` | `/health` | Health check endpoint |
| `POST` | `/upload-excel` | Upload and parse `.xlsx` portfolio spreadsheet |
