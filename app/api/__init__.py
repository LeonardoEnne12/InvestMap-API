from fastapi import APIRouter
from app.api.excel import router as excel_router

api_router = APIRouter()
api_router.include_router(excel_router)

__all__ = ["api_router"]

