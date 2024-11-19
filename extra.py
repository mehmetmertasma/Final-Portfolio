import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

# Example CPU-bound task: Factorial calculation
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example I/O-bound task: Simulate a network request
async def simulated_io_task(task_id, delay):
    print(f"Task {task_id}: Simulating I/O-bound work for {delay} seconds...")
    await asyncio.sleep(delay)
    print(f"Task {task_id}: I/O work complete.")
    return f"I/O Task {task_id} complete"

# Wrapper for CPU-bound task
async def run_cpu_task_in_process_pool(n):
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as executor:
        result = await loop.run_in_executor(executor, factorial, n)
        print(f"Factorial({n}) = {result}")
        return result

# Wrapper for I/O-bound task
async def run_io_task_in_thread_pool(task_id, delay):
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as executor:
        result = await simulated_io_task(task_id, delay)
        return result

# Main coroutine to run tasks
async def main():
    # Scheduling I/O and CPU tasks
    tasks = [
        asyncio.create_task(run_io_task_in_thread_pool(1, 2)),
        asyncio.create_task(run_io_task_in_thread_pool(2, 3)),
        asyncio.create_task(run_cpu_task_in_process_pool(20)),  # Factorial(20)
        asyncio.create_task(run_cpu_task_in_process_pool(15)),  # Factorial(15)
    ]

    # Gathering results
    results = await asyncio.gather(*tasks)
    print("All tasks completed:", results)

# Entry point
if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(f"Execution time: {time.time() - start_time:.2f} seconds")
