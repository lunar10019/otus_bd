import pytest

from library.db import create_customer, get_customer, delete_customer, update_customer


@pytest.fixture
def customer_data():
    return {
        "firstname": "John",
        "lastname": "Doe",
        "email": "john.doe@example.com",
        "telephone": "+1234567890",
        "password": "securepassword123",
    }


def test_create_customer(connection, customer_data):
    customer_id = create_customer(connection, customer_data)
    assert customer_id > 0

    customer = get_customer(connection, customer_id)
    assert customer is not None
    assert customer["firstname"] == customer_data["firstname"]
    assert customer["lastname"] == customer_data["lastname"]
    assert customer["email"] == customer_data["email"]
    assert customer["telephone"] == customer_data["telephone"]

    delete_customer(connection, customer_id)


def test_update_customer(connection, customer_data):
    customer_id = create_customer(connection, customer_data)

    update_data = {
        "firstname": "UpdatedJohn",
        "lastname": "UpdatedDoe",
        "email": "updated.john.doe@example.com",
        "telephone": "+0987654321",
    }
    update_success = update_customer(connection, customer_id, update_data)
    assert update_success is True

    updated_customer = get_customer(connection, customer_id)
    assert updated_customer["firstname"] == update_data["firstname"]
    assert updated_customer["lastname"] == update_data["lastname"]
    assert updated_customer["email"] == update_data["email"]
    assert updated_customer["telephone"] == update_data["telephone"]

    delete_customer(connection, customer_id)


def test_update_nonexistent_customer(connection):
    update_data = {
        "firstname": "NonExistent",
        "lastname": "Customer",
        "email": "nonexistent@example.com",
        "telephone": "+0000000000",
    }
    update_success = update_customer(connection, 999999, update_data)
    assert update_success is False


def test_delete_customer(connection, customer_data):
    customer_id = create_customer(connection, customer_data)

    delete_success = delete_customer(connection, customer_id)
    assert delete_success is True

    deleted_customer = get_customer(connection, customer_id)
    assert deleted_customer is None


def test_delete_nonexistent_customer(connection):
    delete_success = delete_customer(connection, 999999)
    assert delete_success is False
