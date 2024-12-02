import json
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_analyze_pr():
    pr_data = {
        "repo_url": "https://github.com/user/repo",
        "pr_number": 123,
        "github_token": "optional_token"
    }

    response = client.post(
        "/analyze-pr",
        json=pr_data
    )

    assert response.status_code == 200
    assert response.json() == pr_data

def test_analyze_pr_token_none():
    pr_data = {
        "repo_url": "https://github.com/user/repo",
        "pr_number": 123,
        "github_token": None
    }

    response = client.post(
        "/analyze-pr",
        json=pr_data
    )

    assert response.status_code == 200
    assert response.json() == pr_data

def test_analyze_pr_invalid_pr():
    pr_data = {
        "repo_url": "https://github.com/user/repo",
        "pr_number": None,
        "github_token": None
    }

    response = client.post(
        "/analyze-pr",
        json=pr_data
    )

    assert response.status_code == 400
    detail = json.loads(response.content.decode('utf-8'))['detail'][0]
    assert detail['msg']  == f"Input should be a valid integer"

def test_analyze_pr_invalid_url():
    pr_data = {
        "repo_url": 123,
        "pr_number": 123,
        "github_token": None
    }

    response = client.post(
        "/analyze-pr",
        json=pr_data
    )

    assert response.status_code == 400
    detail = json.loads(response.content.decode('utf-8'))['detail'][0]
    assert detail['msg']  == f"Input should be a valid string"
