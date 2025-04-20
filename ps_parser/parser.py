import re


def parse_processes(ps_output):
    processes = []
    for line in ps_output.splitlines()[1:]:
        parts = re.split(r'\s+', line.strip())
        if len(parts) < 11:
            continue

        user = parts[0]
        cpu = float(parts[2])
        mem = float(parts[3])
        command = ' '.join(parts[10:])

        processes.append({
            'user': user,
            'cpu': cpu,
            'mem': mem,
            'command': command[:20] + '...' if len(command) > 20 else command
        })

    return processes


def get_processes():
    import subprocess
    result = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE, text=True)
    return parse_processes(result.stdout)