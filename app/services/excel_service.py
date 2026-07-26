from fastapi import HTTPException, status
from app.domain.excel_models import ExcelUploadResponse
from app.parsers.excel_parser import ExcelParser


class ExcelService:
    """
    Service handling business logic for Excel spreadsheet upload and processing.
    """

    @staticmethod
    def process_excel_upload(filename: str, contents: bytes, content_type: str = None) -> ExcelUploadResponse:
        if not filename.lower().endswith(".xlsx"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid file format. Only Excel files with '.xlsx' extension are accepted."
            )

        if not contents:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Uploaded file is empty."
            )

        try:
            sheets_data = ExcelParser.parse_excel_bytes(contents)
            return ExcelUploadResponse(
                status="success",
                filename=filename,
                content_type=content_type,
                size_bytes=len(contents),
                sheets_found=list(sheets_data.keys()),
                sheets_data=sheets_data
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error parsing Excel file: {str(e)}"
            )
