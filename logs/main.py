import json
import os
import sys
from parser import parse_log_line
from stats import LogStats
from utils import get_log_files, save_stats


def analyze_file(file_path: str):
    print(f"Анализируем {file_path}...")
    stats = LogStats()

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            log_data = parse_log_line(line)
            if log_data:
                stats.process_request(log_data)

    result = stats.get_results()
    print(json.dumps(result, indent=2, ensure_ascii=False))

    output_file = f"{os.path.splitext(file_path)[0]}_stats.json"
    save_stats(result, output_file)
    print(f"Статистика сохранена в {output_file}\n")


def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        log_files = get_log_files(sys.argv[1])
        for log_file in log_files:
            analyze_file(log_file)
    except Exception as e:
        print(f"Ошибка: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
