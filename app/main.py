from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import api_router
from app.repositories import check_db_connection

app = FastAPI(
    title="InvestMap API",
    description="API for investment portfolio management and tracking",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/")
def read_root():
    return {
        "message": "Welcome to InvestMap API",
        "status": "online",
        "docs_url": "/docs"
    }


@app.get("/health")
def health_check():
    db_status = check_db_connection()
    status_str = "ok" if db_status.get("connected") else "degraded"
    return {
        "status": status_str,
        "database": db_status
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
