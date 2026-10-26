from app import app

def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    # Проверяем, что на главной странице есть наш HTML-заголовок
    assert "Веб-приложение для учета тренировок" in response.text

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"