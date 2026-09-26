# Test invalid web requests.
# These checks make sure the API handles bad requests safely.

from app import app


def test_malformed_json():
    client = app.test_client()

    response = client.post(
        "/analyze",
        data="{invalid json",
        content_type="application/json",
    )

    assert response.status_code == 400

    data = response.get_json()

    assert "error" in data


def test_get_analyze_not_allowed():
    client = app.test_client()

    response = client.get("/analyze")

    assert response.status_code == 405


def test_put_analyze_not_allowed():
    client = app.test_client()

    response = client.put(
        "/analyze",
        json={
            "review": "Test review"
        },
    )

    assert response.status_code == 405


def test_unknown_route():
    client = app.test_client()

    response = client.get("/unknown")

    assert response.status_code == 404
