# InvestMap-API Project Context & Memory

> **Note for AI Assistant:** This file registers the ongoing architecture, goals, state, and endpoints of InvestMap-API. Read and update this document whenever major alterations or feature additions occur to optimize token usage and keep repository context concise.

---

## 📌 Project Overview
- **Name:** InvestMap-API
- **Goal:** Backend API for investment tracking and management. Enables uploading portfolio spreadsheets (Excel `.xlsx`), parsing asset data, and analyzing investment metrics.
- **Tech Stack:** Python 3.10+, FastAPI, Uvicorn, OpenPyXL, Pydantic.

---

## 🛠️ Architecture & Endpoints

### Application Structure
```
InvestMap-API/
├── app/
│   ├── __init__.py
│   ├── main.py               # Main FastAPI entrypoint & router configuration
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── excel.py       # Excel upload routes (POST /upload-excel)
│   ├── domain/
│   │   ├── __init__.py
│   │   └── excel_models.py # Pydantic schemas (ExcelUploadResponse, SheetSummary)
│   ├── parsers/
│   │   ├── __init__.py
│   │   └── excel_parser.py # openpyxl spreadsheet parsing service
│   ├── services/
│   │   ├── __init__.py
│   │   └── excel_service.py# Excel processing business service
│   └── repositories/
│       └── __init__.py        # Data access repository interfaces & storage logic
├── tests/
│   └── unit/
│       ├── test_excel_parser.py # Unit tests for parser
│       └── test_excel_api.py    # Integration tests for upload endpoints
├── .agents/
│   └── AGENTS.md             # Project context & AI memory (this file)
├── .gitignore                # Git ignore rules
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

### Active Endpoints
- `GET /`: Health check / welcome message.
- `GET /health`: System health check.
- `POST /upload-excel`: Receives a `.xlsx` spreadsheet file, validates format, parses sheet metadata and preview data via `app.services.ExcelService`.

---

## 📝 Recent Activity Log
- **2026-07-25:** Removed root `main.py` proxy script and upgraded `README.md` with full installation, execution (`uvicorn app.main:app --reload`), testing, and API instructions.
- **2026-07-25:** Refactored project structure to modular layered architecture (`app/` package with `api/`, `services/`, `parsers/`, `domain/`, `repositories/` and unit test organization under `tests/unit/`).
- **2026-07-25:** Initialized project structure with FastAPI, `.gitignore`, `.agents/AGENTS.md`, `requirements.txt`, and `POST /upload-excel` endpoint for handling `.xlsx` Excel uploads.
