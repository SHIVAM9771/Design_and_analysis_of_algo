import numpy as np
import timeit


def russian_peasant_multiplication(n1, n2):
    prod = np.int64(0)
    while n1 >= 1:
        if n1 % 2 == 1:
            prod += n2
        n1 //= 2
        n2 *= 2
    return prod


def benchmark(trials=5000):
    n1_vals = np.random.randint(2500, 50000, size=trials, dtype=np.int64)
    n2_vals = np.random.randint(25000, 500000, size=trials, dtype=np.int64)

    def run_trials():
        for i in range(trials):
            russian_peasant_multiplication(n1_vals[i], n2_vals[i])

    elapsed_time = timeit.timeit(run_trials, number=1)
    avg_time = (elapsed_time / trials) * 1e6
    return avg_time


if __name__ == "__main__":
    num_experiments = 2500
    avg_times = np.array([benchmark(trials=5000) for _ in range(num_experiments)])

    overall_avg = np.mean(avg_times)
    print(round(overall_avg, 2))
