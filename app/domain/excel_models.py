from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class SheetSummary(BaseModel):
    total_rows: int = Field(..., description="Total data rows in sheet (excluding header)")
    total_columns: int = Field(..., description="Total columns in sheet")
    columns: List[str] = Field(default_factory=list, description="Column names")
    preview_sample: List[Dict[str, Any]] = Field(default_factory=list, description="Top sample rows")


class ExcelUploadResponse(BaseModel):
    status: str = Field("success", description="Status of the operation")
    filename: str = Field(..., description="Uploaded file name")
    content_type: Optional[str] = Field(None, description="MIME content type")
    size_bytes: int = Field(..., description="File size in bytes")
    sheets_found: List[str] = Field(default_factory=list, description="List of sheet names found")
    sheets_data: Dict[str, SheetSummary] = Field(default_factory=dict, description="Summary data per sheet")
