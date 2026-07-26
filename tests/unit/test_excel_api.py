import io
import openpyxl
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"
    print("[OK] test_root_endpoint passed")


def test_upload_excel_invalid_extension():
    files = {"file": ("invalid.txt", b"text content", "text/plain")}
    response = client.post("/upload-excel", files=files)
    assert response.status_code == 400
    assert "Invalid file format" in response.json()["detail"]
    print("[OK] test_upload_excel_invalid_extension passed")


def test_upload_excel_valid_file():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Portfolio"
    ws.append(["Asset", "Price"])
    ws.append(["ITUB4", 31.50])

    buf = io.BytesIO()
    wb.save(buf)
    wb.close()

    files = {
        "file": (
            "portfolio.xlsx",
            buf.getvalue(),
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    }

    response = client.post("/upload-excel", files=files)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["filename"] == "portfolio.xlsx"
    assert "Portfolio" in data["sheets_found"]
    assert data["sheets_data"]["Portfolio"]["total_rows"] == 1
    print("[OK] test_upload_excel_valid_file passed")


if __name__ == "__main__":
    print("Running API Unit Tests...")
    test_root_endpoint()
    test_upload_excel_invalid_extension()
    test_upload_excel_valid_file()
    print("API Unit Tests Completed Successfully!")
