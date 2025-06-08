import socket
from .request import parse_request, parse_status_code
from .response import build_response


def run_server(host="127.0.0.1", port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server running on http://{host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            handle_connection(conn, addr)


def handle_connection(conn, addr):
    with conn:
        try:
            data = conn.recv(1024)
            if not data:
                return

            method, path, headers = parse_request(data)
            status_code = parse_status_code(path)
            response = build_response(method, addr, status_code, headers)
            conn.sendall(response.encode())
        except Exception as e:
            print(f"Error handling connection: {e}")
            error_response = "HTTP/1.1 500 Internal Server Error\r\n\r\n"
            conn.sendall(error_response.encode())
