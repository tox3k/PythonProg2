import os

def process_count(username: str) -> int:
    data = os.popen(f'ps --user {username} | wc -l').read()
    return int(data) - 1

def total_memory_usage(root_pid: int) -> float:
    process_mem = float(os.popen(f'ps -v {root_pid}').readlines()[1].split()[8])
    data = os.popen(f'ps -v --ppid {root_pid}').readlines()[1:]
    raw_arr = list(map(str.split ,data))
    memory = sum(list(float(i[8]) for i in raw_arr))
    
    return process_mem + memory

print(f'Root process count: {process_count("root")}')
print(f'Total memory usage of process_pid 40970 (Firefox): {total_memory_usage(40970)}')