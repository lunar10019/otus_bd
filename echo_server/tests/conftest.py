import pytest
from threading import Thread
import time
from echo_server.server import run_server


@pytest.fixture(scope="module")
def echo_server():
    server_thread = Thread(target=run_server, daemon=True)
    server_thread.start()
    time.sleep(0.1)
    yield
