import multiprocessing
import os
import time

def cpu_load():
    while True:
        pass  # Infinite loop to load the CPU

def memory_load(size_in_gb):
    large_list = []
    size_in_bytes = size_in_gb * 1024**3
    num_elements = size_in_bytes // 8  # Number of 8-byte elements to allocate
    try:
        large_list = [0] * num_elements
    except MemoryError:
        print("Memory allocation failed")
    time.sleep(3600)  # Sleep for 1 hour to keep the memory allocated

if __name__ == "__main__":
    num_cpus = multiprocessing.cpu_count()
    size_in_gb = int(input("Enter the amount of memory to allocate in GB: "))

    print(f"Loading CPU with {num_cpus} cores.")
    print(f"Allocating {size_in_gb} GB of RAM.")

    cpu_processes = []

    try:
        for _ in range(num_cpus):
            p = multiprocessing.Process(target=cpu_load)
            p.start()
            cpu_processes.append(p)

        memory_process = multiprocessing.Process(target=memory_load, args=(size_in_gb,))
        memory_process.start()

        for p in cpu_processes:
            p.join()
        memory_process.join()

    except KeyboardInterrupt:
        print("Terminating the load processes")
        for p in cpu_processes:
            p.terminate()
        memory_process.terminate()
