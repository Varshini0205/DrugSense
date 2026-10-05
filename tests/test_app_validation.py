# Test Flask input limits.
# These checks make sure very long reviews are rejected.

from app import app


def test_review_too_long():
    client = app.test_client()

    review = "a" * 10001

    response = client.post(
        "/analyze",
        json={
            "review": review
        },
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "Review is too long."


def test_review_at_limit():
    client = app.test_client()

    review = "a" * 10000

    response = client.post(
        "/analyze",
        json={
            "review": review
        },
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "prediction" in data
