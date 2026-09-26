# Test the analytics endpoint.
# These checks make sure the dashboard statistics are available.

from app import app


def test_stats_endpoint():

    client = app.test_client()

    response = client.get("/api/stats")

    assert response.status_code == 200

    data = response.get_json()

    assert "dataset" in data
    assert "model" in data
    assert "comparison" in data
    assert "nlp_modules" in data

    assert data["model"]["accuracy"] > 0
    assert data["model"]["macro_f1"] > 0
    assert data["model"]["weighted_f1"] > 0
