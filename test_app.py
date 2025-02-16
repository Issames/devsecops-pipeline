import app

def test_hello():
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, DevSecOps!" in response.data