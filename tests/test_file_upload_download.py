import os
def test_file_upload(session):
    file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
    with open(file_path, "rb") as f:
        files = {"file": f}
        response = session.post("https://postman-echo.com/post", files=files)

    assert response.status_code == 200
    json_data = response.json()
    assert "data" in json_data
    assert "This is a test file for upload." in json_data["data"]  # check file content in raw data


def test_file_download(session, tmp_path):
    url = "https://postman-echo.com/get?test=image"
    response = session.get(url)
    assert response.status_code == 200
    
    file_path = tmp_path / "downloaded.png"
    with open(file_path, "wb") as f:
        f.write(response.content)

    # Validate file saved
    assert file_path.exists()
    assert file_path.stat().st_size > 0
