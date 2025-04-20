from datetime import datetime


def generate_report(analysis):
    report = ["Отчёт о состоянии системы:", f"Пользователи системы: {', '.join(analysis['users'])}",
              f"Процессов запущено: {analysis['total_processes']}", "\nПользовательских процессов:"]

    for user, count in sorted(analysis['user_process_counts'].items()):
        report.append(f"{user}: {count}")

    report.append(f"\nВсего памяти используется: {analysis['avg_mem']:.1f}%")
    report.append(f"Всего CPU используется: {analysis['avg_cpu']:.1f}%")
    report.append(
        f"Больше всего памяти использует: {analysis['max_mem_process']['command']} "
        f"({analysis['max_mem_process']['mem']:.1f}%)"
    )
    report.append(
        f"Больше всего CPU использует: {analysis['max_cpu_process']['command']} "
        f"({analysis['max_cpu_process']['cpu']:.1f}%)"
    )

    return '\n'.join(report)


def save_report(report_text):
    filename = datetime.now().strftime("%d-%m-%Y-%H:%M") + "-scan.txt"
    with open(filename, 'w') as f:
        f.write(report_text)
    return filename