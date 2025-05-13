import socket


def validate_port(port):
    return 0 < port < 65536


def get_available_port(start_port=5000):
    port = start_port
    while port < 65536:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(("", port))
                return port
        except OSError:
            port += 1
    raise OSError("No available ports found")
