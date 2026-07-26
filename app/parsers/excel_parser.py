import io
from typing import Dict
import openpyxl
from app.domain.excel_models import SheetSummary


class ExcelParser:
    """
    Parser for reading Excel (.xlsx) files using openpyxl.
    """

    @staticmethod
    def parse_excel_bytes(file_bytes: bytes, preview_limit: int = 5) -> Dict[str, SheetSummary]:
        stream = io.BytesIO(file_bytes)
        wb = openpyxl.load_workbook(stream, data_only=True)
        sheets_summary: Dict[str, SheetSummary] = {}

        for sheet_name in wb.sheetnames:
            ws = wb[sheet_name]
            rows = list(ws.iter_rows(values_only=True))

            if not rows:
                sheets_summary[sheet_name] = SheetSummary(
                    total_rows=0,
                    total_columns=0,
                    columns=[],
                    preview_sample=[]
                )
                continue

            header_row = [str(col) if col is not None else f"Column_{i+1}" for i, col in enumerate(rows[0])]
            data_rows = [r for r in rows[1:] if any(cell is not None for cell in r)]

            preview = []
            for row in data_rows[:preview_limit]:
                row_dict = {}
                for idx, col_name in enumerate(header_row):
                    val = row[idx] if idx < len(row) else None
                    row_dict[col_name] = val
                preview.append(row_dict)

            sheets_summary[sheet_name] = SheetSummary(
                total_rows=len(data_rows),
                total_columns=len(header_row),
                columns=header_row,
                preview_sample=preview
            )

        wb.close()
        return sheets_summary
