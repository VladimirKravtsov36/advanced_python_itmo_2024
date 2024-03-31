import math
import multiprocessing
import concurrent.futures
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def integrate(f, a, b, *, n_jobs, executor=concurrent.futures.ThreadPoolExecutor, n_iter=1000000):
    acc = 0
    step = (b - a) / n_iter
    logging.info(f'Starting integration with {n_jobs} job(s)')
    with executor(max_workers=n_jobs) as executor:
        f_args = [(f, a + i * step, a + (i + 1) * step, step) for i in range(n_iter)]
        results = list(executor.map(calculate_integral, f_args))
        for result in results:
            acc += result
    return acc


def calculate_integral(*args):
    f = args[0][0]
    a = args[0][1]
    step = args[0][-1]
    return f(a) * step

if __name__ == "__main__":
    
    n_jobs_list = [1, 4, 8, 16, 20]

    with open("artifacts/4.2.txt", "w") as file:
        file.write("n_jobs\tThreadPoolExecutor\tProcessPoolExecutor\n")

        for n_jobs in n_jobs_list:
            logging.info(f'Starting ThreadPoolExecutor with {n_jobs} job(s)')
            start_time = time.time()
            integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, executor=concurrent.futures.ThreadPoolExecutor)
            thread_pool_time = time.time() - start_time
            logging.info(f'ThreadPoolExecutor with {n_jobs} jobs finished in {thread_pool_time:.2f} seconds')

            logging.info(f'Starting ProcessPoolExecutor with {n_jobs} jobs')
            start_time = time.time()
            integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, executor=concurrent.futures.ProcessPoolExecutor)
            process_pool_time = time.time() - start_time
            logging.info(f'ProcessPoolExecutor with {n_jobs} jobs finished in {process_pool_time:.2f} seconds')

            file.write(f"{n_jobs}\t{thread_pool_time}\t{process_pool_time}\n")
