import io
import openpyxl
from app.parsers.excel_parser import ExcelParser


def test_excel_parser_extracts_sheets_and_rows():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Assets"

    ws.append(["Ticker", "Amount"])
    ws.append(["PETR4", 100])
    ws.append(["VALE3", 200])

    buf = io.BytesIO()
    wb.save(buf)
    wb.close()

    result = ExcelParser.parse_excel_bytes(buf.getvalue())
    assert "Assets" in result
    assert result["Assets"].total_rows == 2
    assert result["Assets"].total_columns == 2
    assert result["Assets"].columns == ["Ticker", "Amount"]
    assert result["Assets"].preview_sample[0]["Ticker"] == "PETR4"
    print("[OK] test_excel_parser_extracts_sheets_and_rows passed")


if __name__ == "__main__":
    test_excel_parser_extracts_sheets_and_rows()
