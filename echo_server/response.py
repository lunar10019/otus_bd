from http import HTTPStatus


def build_response(method, addr, status_code, headers):
    status_phrase = get_status_phrase(status_code)

    response_body = [
        f"Request Method: {method}",
        f"Request Source: {addr}",
        f"Response Status: {status_code} {status_phrase}",
        *[f"{k}: {v}" for k, v in headers.items()],
    ]

    response_body = "\n".join(response_body)

    response_headers = [
        f"HTTP/1.1 {status_code} {status_phrase}",
        "Content-Type: text/plain; charset=utf-8",
        f"Content-Length: {len(response_body)}",
        "Connection: close",
        "",
        response_body,
    ]

    return "\r\n".join(response_headers)


def get_status_phrase(status_code):
    try:
        return HTTPStatus(status_code).phrase
    except ValueError:
        return HTTPStatus(200).phrase
