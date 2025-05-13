from typing import Optional, Dict
from config import LOG_PATTERN


def parse_log_line(line: str) -> Optional[Dict]:
    match = LOG_PATTERN.match(line.strip())
    if not match:
        return None

    data = match.groupdict()

    try:
        data["status"] = int(data["status"])
        data["bytes"] = 0 if data["bytes"] == "-" else int(data["bytes"])
        data["duration"] = int(data["duration"])
    except (ValueError, TypeError):
        return None

    return data
