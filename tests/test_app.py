from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_from_activity():
    response = client.post(
        "/activities/Chess Club/signup?email=teststudent@mergington.edu"
    )
    assert response.status_code == 200

    response = client.delete("/activities/Chess Club/unregister?email=teststudent@mergington.edu")
    assert response.status_code == 200
    assert response.json()["message"] == "Unregistered teststudent@mergington.edu from Chess Club"

    response = client.delete("/activities/Chess Club/unregister?email=teststudent@mergington.edu")
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"
