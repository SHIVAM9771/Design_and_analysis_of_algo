import timeit
import matplotlib.pyplot as plt
import random

# Global Variable
N = []
CPU = []


# Main program
def linearSearch():
    res = False
    # trail = int(input("Enter no. of trails: "))  # Number of trials
    trail = random.randint(1, 50)
    for i in range(trail):
        print("TRAIL NO:", i + 1)
        # n = int(input("Enter No. of elements in the array: "))  # Array size
        n = random.randint(1, 50)
        Array = [random.randint(1, 100) for _ in range(n)]  # Generate random array
        print(f"Array of size {n}: {Array[:]}")  # Print first 10 elements for reference
        key = random.choice(Array)  # Randomly choose a key to search

        # Measure time taken for the linear search
        start = timeit.default_timer()
        for x in range(n):
            if Array[x] == key:
                res = True
        times = timeit.default_timer() - start
        print("Key Found:", "True" if res else "False")

        N.append(n)
        CPU.append(round(float(times) * 1_000_000, 2))
    print("N CPU")
    for t in range(0, trail):
        print(N[t], CPU[t])

    # Plotting Graph
    plt.plot(N, CPU, label="Linear Search Time", color="blue", marker="o")
    plt.scatter(N, CPU, color="red", marker="*", s=50)

    # Labeling the x and y axis
    plt.xlabel("Array Size - N")
    plt.ylabel("CPU Processing Time (seconds)")
    plt.title("Linear Search Time Efficiency")

    # Add grid for better visualization
    plt.grid(True)

    # Show the plot
    plt.show()


linearSearch()
