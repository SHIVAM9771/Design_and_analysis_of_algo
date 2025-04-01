import timeit
import matplotlib.pyplot as plt


# Binary Search Function
def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False


# Main Block
N, CPU = [], []
trials = int(input("Enter number of trials: "))

for t in range(trials):
    n = int(input(f"Trial {t+1} - Enter number of elements: "))
    arr = sorted([int(input("Enter element: ")) for _ in range(n)])
    key = int(input("Enter key: "))

    start = timeit.default_timer()
    print("Element Found:", binary_search(arr, key))
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
plt.title("Binary Search Time Efficiency")
plt.show()
