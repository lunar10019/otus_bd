import re

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) - - \[(?P<date>.+?)\] "(?P<method>\S+) (?P<url>\S+) (?P<protocol>\S+)" '
    r'(?P<status>\d+) (?P<bytes>\S+) "(?P<referer>.*?)" "(?P<user_agent>.*?)" (?P<duration>\d+)'
)

HTTP_METHODS = {"GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD"}
