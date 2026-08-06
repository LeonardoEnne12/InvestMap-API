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


def test_excel_parser_filters_empty_and_total_rows():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Portfolio"

    ws.append(["Produto", "Instituição", "Valor Atualizado"])
    ws.append(["CDB C6", "C6 Bank", 1000.0])
    # Empty string + nulls row
    ws.append(["", None, None])
    # Total summary row
    ws.append(["", "", "Total"])
    # Empty product name with numeric grand total sum row
    ws.append(["", "", 23298.06])

    buf = io.BytesIO()
    wb.save(buf)
    wb.close()

    result = ExcelParser.parse_excel_bytes(buf.getvalue())
    assert result["Portfolio"].total_rows == 1
    assert len(result["Portfolio"].preview_sample) == 1
    assert result["Portfolio"].preview_sample[0]["Produto"] == "CDB C6"
    print("[OK] test_excel_parser_filters_empty_and_total_rows passed")


if __name__ == "__main__":
    test_excel_parser_extracts_sheets_and_rows()
    test_excel_parser_filters_empty_and_total_rows()

