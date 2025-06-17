import pytest

from library.db import get_customer, update_customer, delete_customer, create_customer


def test_create_customer(test_customer, connection, customer_data):
    customer = get_customer(connection, test_customer)
    assert customer is not None
    assert customer["firstname"] == customer_data["firstname"]
    assert customer["lastname"] == customer_data["lastname"]
    assert customer["email"] == customer_data["email"]
    assert customer["telephone"] == customer_data["telephone"]


def test_update_customer(test_customer, connection):
    update_data = {
        "firstname": "UpdatedJohn",
        "lastname": "UpdatedDoe",
        "email": "updated.john.doe@example.com",
        "telephone": "+0987654321",
    }
    update_success = update_customer(connection, test_customer, update_data)
    assert update_success is True

    updated_customer = get_customer(connection, test_customer)
    assert updated_customer["firstname"] == update_data["firstname"]
    assert updated_customer["lastname"] == update_data["lastname"]
    assert updated_customer["email"] == update_data["email"]
    assert updated_customer["telephone"] == update_data["telephone"]


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
