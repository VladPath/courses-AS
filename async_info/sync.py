import time
from tracemalloc import start

# CPU задаче

def process_data():
    x = 2**50
    time.sleep(1)

def generate_report():
    time.sleep(2)

# В синхронных функциях выполнение последовательно
def main():
    start_time = time.perf_counter()
    process_data()
    generate_report()
    finish_time = time.perf_counter()
    print(f"Времени прошло: {finish_time-start_time}")

if __name__ == '__main__':
    main()