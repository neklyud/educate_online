import pytest   
from main import app
from fastapi.testclient import TestClient
import logging

client = TestClient(app)

def test_assert():
    response = client.get('/docs')
    assert response.status_code == 200

def test_post_success():
    response = client.post('/calc', json={'number1': 1, 'number2': 2})
    assert response.status_code == 200
    assert response.json() == {'result': 3}

def test_post_failure():
    response = client.post('/calc', json={'number1': -1, 'number2': 0})
    assert response.status_code == 422

def test_post_failure_2():
    response = client.post('/calc', json={'number1': 1, 'number2': -1})
    assert response.status_code == 422
