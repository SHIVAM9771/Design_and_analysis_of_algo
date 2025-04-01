import timeit
import matplotlib.pyplot as plt


# Selection Sort Function
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Main Block
N, CPU = [], []
trials = int(input("Enter number of trials: "))

for t in range(trials):
    n = int(input(f"Trial {t+1} - Enter number of elements: "))
    arr = [int(input("Enter element: ")) for _ in range(n)]

    start = timeit.default_timer()
    selection_sort(arr)
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
plt.title("Selection Sort Time Efficiency")
plt.show()


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_ind = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[min_ind], arr[i] = arr[i], arr[min_ind]
