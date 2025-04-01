import timeit
import matplotlib.pyplot as plt
import random
import sys
import tracemalloc

# Tower of Hanoi function
def towerOfHanoi(n, src, des, aux):
    if n == 0:
        return
    towerOfHanoi(n - 1, src, aux, des)
    towerOfHanoi(n - 1, aux, des, src)

N, CPU, MEMORY = [], [], []

# Run multiple trials with random disk sizes
for _ in range(random.randint(5, 25)):
    n = random.randint(20, 150)

    # Measure time
    start_time = timeit.default_timer()
    tracemalloc.start()  # Start memory tracking

    towerOfHanoi(n, "A", "B", "C")

    end_time = timeit.default_timer()
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    N.append(n)
    CPU.append(round((end_time - start_time) * 1e6, 2))
    MEMORY.append(peak_memory)

# Display time and memory usage
print("\nN\tCPU (microseconds)\tMemory (bytes)")
for n, cpu, mem in zip(N, CPU, MEMORY):
    print(f"{n}\t{cpu}\t\t\t{mem}")

# Plot time and memory performance
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(N, CPU, marker="o", color="blue", linestyle="--", linewidth=1, markersize=6)
plt.xlabel("Number of Disks (N)")
plt.ylabel("CPU Time (microseconds)")
plt.title("Tower of Hanoi Time Efficiency")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(N, MEMORY, marker="o", color="red", linestyle="--", linewidth=1, markersize=6)
plt.xlabel("Number of Disks (N)")
plt.ylabel("Memory Usage (bytes)")
plt.title("Tower of Hanoi Space Efficiency")
plt.grid(True)

plt.tight_layout()
plt.show()
