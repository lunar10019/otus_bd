import pytest
import pymysql

from library.db import create_customer, get_customer, delete_customer


def pytest_addoption(parser):
    parser.addoption(
        "--host", action="store", default="localhost", help="Database host"
    )
    parser.addoption(
        "--port", action="store", type=int, default=3306, help="Database port"
    )
    parser.addoption(
        "--database", action="store", default="opencart", help="Database name"
    )
    parser.addoption("--user", action="store", default="root", help="Database user")
    parser.addoption("--password", action="store", default="", help="Database password")


@pytest.fixture(scope="session")
def connection(request):
    host = request.config.getoption("--host")
    port = request.config.getoption("--port")
    database = request.config.getoption("--database")
    user = request.config.getoption("--user")
    password = request.config.getoption("--password")

    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        cursorclass=pymysql.cursors.DictCursor,
    )

    yield conn

    conn.close()


@pytest.fixture
def customer_data():
    return {
        "firstname": "John",
        "lastname": "Doe",
        "email": "john.doe@example.com",
        "telephone": "+1234567890",
        "password": "securepassword123",
    }


@pytest.fixture
def test_customer(connection, customer_data):
    customer_id = create_customer(connection, customer_data)
    yield customer_id

    if get_customer(connection, customer_id):
        delete_customer(connection, customer_id)
