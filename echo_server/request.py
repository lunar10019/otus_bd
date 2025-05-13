from urllib.parse import parse_qs, urlparse


def parse_request(data):
    request_lines = data.decode().split("\r\n")
    request_line = request_lines[0]
    method, path, _ = request_line.split()

    headers = {}
    for line in request_lines[1:]:
        if not line:
            break
        key, value = line.split(": ", 1)
        headers[key] = value

    return method, path, headers


def parse_status_code(path):
    try:
        query = urlparse(path).query
        params = parse_qs(query)
        if "status" in params:
            return int(params["status"][0])
    except (ValueError, KeyError):
        pass
    return 200
