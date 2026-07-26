from fastapi import APIRouter
from app.api.v1.excel import router as excel_router

api_v1_router = APIRouter()
api_v1_router.include_router(excel_router)

__all__ = ["api_v1_router"]
