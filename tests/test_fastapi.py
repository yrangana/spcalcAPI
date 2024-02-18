from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_calculate_add():
    response = client.post(
        "/calculate", json={"number1": 5, "number2": 10, "operation": "add"}
    )
    assert response.status_code == 200
    assert response.json() == {"answer": 15}


def test_calculate_subtract():
    response = client.post(
        "/calculate", json={"number1": 10, "number2": 5, "operation": "subtract"}
    )
    assert response.status_code == 200
    assert response.json() == {"answer": 5}


def test_calculate_multiply():
    response = client.post(
        "/calculate", json={"number1": 5, "number2": 10, "operation": "multiply"}
    )
    assert response.status_code == 200
    assert response.json() == {"answer": 50}


def test_calculate_divide():
    response = client.post(
        "/calculate", json={"number1": 10, "number2": 5, "operation": "divide"}
    )
    assert response.status_code == 200
    assert response.json() == {"answer": 2}


def test_calculate_invalid_operation():
    response = client.post(
        "/calculate", json={"number1": 10, "number2": 5, "operation": "invalid"}
    )
    assert response.status_code == 400
    assert response.json() == {
        "error": "Invalid operation, please use add, subtract, multiply or divide"
    }


def test_calculate_divide_by_zero():
    response = client.post(
        "/calculate", json={"number1": 10, "number2": 0, "operation": "divide"}
    )
    assert response.status_code == 400
    assert response.json() == {"error": "Cannot divide by zero"}
