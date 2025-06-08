from parser import get_processes
from analyzer import analyze_processes
from reporter import generate_report, save_report


def main():
    processes = get_processes()

    analysis = analyze_processes(processes)

    report = generate_report(analysis)

    print(report)

    filename = save_report(report)
    print(f"\nОтчёт сохранён в файл: {filename}")


if __name__ == "__main__":
    main()
