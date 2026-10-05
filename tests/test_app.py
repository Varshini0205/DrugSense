# Test the Flask web routes.
# These checks make sure the API accepts and rejects reviews correctly.

from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"DrugSense" in response.data


def test_analyze_review():
    client = app.test_client()

    response = client.post(
        "/analyze",
        json={
            "review": (
                "Metformin helped my diabetes "
                "but caused severe nausea."
            )
        },
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "prediction" in data
    assert data["prediction"]["condition"] is not None


def test_analyze_entities():
    client = app.test_client()

    response = client.post(
        "/analyze",
        json={
            "review": (
                "Metformin helped my diabetes "
                "but caused nausea."
            )
        },
    )

    data = response.get_json()

    assert "entities" in data
    assert "metformin" in data["entities"]["drugs"]
    assert "diabetes" in data["entities"]["conditions"]
    assert "nausea" in data["entities"]["symptoms"]


def test_empty_review():
    client = app.test_client()

    response = client.post(
        "/analyze",
        json={
            "review": ""
        },
    )

    assert response.status_code == 400

    data = response.get_json()

    assert "error" in data


def test_missing_review():
    client = app.test_client()

    response = client.post(
        "/analyze",
        json={}
    )

    assert response.status_code == 400

    data = response.get_json()

    assert "error" in data


def test_invalid_review_type():
    client = app.test_client()

    response = client.post(
        "/analyze",
        json={
            "review": 12345
        },
    )

    assert response.status_code == 400

    data = response.get_json()

    assert "error" in data


def test_no_json():
    client = app.test_client()

    response = client.post("/analyze")

    assert response.status_code == 400

    data = response.get_json()

    assert "error" in data
