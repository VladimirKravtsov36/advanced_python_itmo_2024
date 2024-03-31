import threading
import multiprocessing
import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def run_sync(n):
    start_time = time.time()
    for _ in range(10):
        fibonacci(n)
    return time.time() - start_time

def run_threads(n):
    start_time = time.time()
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=fibonacci, args=(n,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return time.time() - start_time

def run_processes(n):
    start_time = time.time()
    processes = []
    for _ in range(10):
        process = multiprocessing.Process(target=fibonacci, args=(n,))
        process.start()
        processes.append(process)
    for process in processes:
        process.join()
    return time.time() - start_time

if __name__ == "__main__":
    n = 40  
    sync_time = run_sync(n)
    thread_time = run_threads(n)
    process_time = run_processes(n)

    with open("artifacts/4.1.txt", "w") as file:
        file.write(f"Sync Time: {sync_time}\n")
        file.write(f"Thread Time: {thread_time}\n")
        file.write(f"Process Time: {process_time}")
