import os
import json
from typing import List, Dict


def get_log_files(path: str) -> List[str]:
    if os.path.isfile(path):
        return [path]
    elif os.path.isdir(path):
        return [
            os.path.join(path, f)
            for f in os.listdir(path)
            if os.path.isfile(os.path.join(path, f))
        ]
    raise ValueError(f"Путь {path} не является файлом или директорией")


def save_stats(stats: Dict, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
