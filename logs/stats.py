from collections import defaultdict
from typing import Dict
from config import HTTP_METHODS


class LogStats:
    def __init__(self):
        self.total_requests = 0
        self.ip_counts = defaultdict(int)
        self.method_counts = defaultdict(int)
        self.requests = []

    def process_request(self, log_data: Dict):
        self.total_requests += 1
        self.ip_counts[log_data["ip"]] += 1

        method = log_data["method"]
        if method in HTTP_METHODS:
            self.method_counts[method] += 1
        else:
            self.method_counts["OTHER"] += 1

        self.requests.append(
            {
                "ip": log_data["ip"],
                "date": f"[{log_data['date']}]",
                "method": log_data["method"],
                "url": log_data["url"],
                "duration": log_data["duration"],
            }
        )

    def get_results(self) -> Dict:
        top_ips = dict(
            sorted(self.ip_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        )

        top_longest = sorted(self.requests, key=lambda x: x["duration"], reverse=True)[
            :3
        ]

        return {
            "total_requests": self.total_requests,
            "total_stat": dict(self.method_counts),
            "top_ips": top_ips,
            "top_longest": top_longest,
        }
