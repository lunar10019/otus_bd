from collections import defaultdict


def analyze_processes(processes):
    users = set()
    user_process_count = defaultdict(int)
    total_mem = 0.0
    total_cpu = 0.0
    max_mem_process = {'mem': 0, 'command': ''}
    max_cpu_process = {'cpu': 0, 'command': ''}

    for p in processes:
        users.add(p['user'])
        user_process_count[p['user']] += 1
        total_mem += p['mem']
        total_cpu += p['cpu']

        if p['mem'] > max_mem_process['mem']:
            max_mem_process = {'mem': p['mem'], 'command': p['command']}

        if p['cpu'] > max_cpu_process['cpu']:
            max_cpu_process = {'cpu': p['cpu'], 'command': p['command']}

    return {
        'users': sorted(users),
        'total_processes': len(processes),
        'user_process_counts': dict(user_process_count),
        'avg_mem': total_mem / len(processes),
        'avg_cpu': total_cpu / len(processes),
        'max_mem_process': max_mem_process,
        'max_cpu_process': max_cpu_process
    }