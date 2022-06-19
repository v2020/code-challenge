def test_dashboard_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_vulnerabilities_page(client):
    response = client.get("/vulnerabilities/")
    assert response.status_code == 200


def test_error_404(client):
    response = client.get("/404testpage/")
    assert response.status_code == 404
