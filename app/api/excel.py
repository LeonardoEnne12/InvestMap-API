from fastapi import APIRouter, File, UploadFile
from app.domain.excel_models import ExcelUploadResponse
from app.services.excel_service import ExcelService

router = APIRouter(tags=["Excel"])


@router.post("/upload-excel", response_model=ExcelUploadResponse)
async def upload_excel(file: UploadFile = File(...)) -> ExcelUploadResponse:

    filename = file.filename or ""
    contents = await file.read()
    return ExcelService.process_excel_upload(
        filename=filename,
        contents=contents,
        content_type=file.content_type
    )
