# 1. Write a program to implement linear search algorithm. Repeat the experiment for
# different values of n, the number of elements in the list to be searched and plot a
# graph of time taken versus n.

import timeit
import matplotlib.pyplot as plt


# Linear Search Function
def linear_search(arr, key):
    for x in arr:
        if x == key:
            return True
    return False


# Main Block
N, CPU = [], []
trials = int(input("Enter number of trials: "))

for t in range(trials):
    n = int(input(f"Trial {t+1} - Enter number of elements: "))
    arr = [int(input("Enter element: ")) for _ in range(n)]
    key = int(input("Enter key: "))

    start = timeit.default_timer()
    print("Element Found:", linear_search(arr, key))
    times = timeit.default_timer() - start

    N.append(n)
    CPU.append(round(times * 1e6, 2))

# Display Results
print("\nN\tCPU Time (µs)")
for n, time in zip(N, CPU):
    print(f"{n}\t{time}")

# Plot Graph
plt.plot(N, CPU, marker="o", color="red")
plt.xlabel("Array Size (N)")
plt.ylabel("CPU Time (µs)")
plt.title("Linear Search Time Efficiency")
plt.show()
