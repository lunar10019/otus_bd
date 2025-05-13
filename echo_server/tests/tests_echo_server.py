import pytest
import socket

from echo_server.utils import validate_port, get_available_port


@pytest.mark.parametrize(
    "port, expected",
    [
        (5000, True),
        (80, True),
        (65535, True),
        (0, False),
        (-1, False),
        (65536, False),
    ],
)
def test_validate_port(port, expected):
    assert validate_port(port) == expected


def test_get_available_port():
    port = get_available_port()
    assert validate_port(port) is True


def test_server_response(echo_server):
    response = send_test_request("GET", "/")
    assert "Request Method: GET" in response
    assert "HTTP/1.1 200 OK" in response


@pytest.mark.parametrize(
    "status,expected",
    [
        (200, "200 OK"),
        (404, "404 Not Found"),
        (500, "500 Internal Server Error"),
    ],
)
def test_status_codes(echo_server, status, expected):
    response = send_test_request("GET", f"/?status={status}")
    print(response)
    assert f"HTTP/1.1 {expected}" in response
    assert f"Response Status: {status}" in response


# Вспомогательная функция для тестов
def send_test_request(method="GET", path="/", headers=None):
    if headers is None:
        headers = {}

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 5000))
        request = f"{method} {path} HTTP/1.1\r\n"
        for k, v in headers.items():
            request += f"{k}: {v}\r\n"
        request += "\r\n"
        s.sendall(request.encode())

        response = b""
        while True:
            part = s.recv(4096)
            if not part:
                break
            response += part

        return response.decode()
