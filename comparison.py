import time
import gc


def measure_perf_per_iter(num_iterations: int, func: list, *args):
    """
    Measures the runtime and memory usage of a function for each iteration.

    :param func: The function to measure.
    :param args: Arguments to pass to the function.
    :return: A tuple (average_time_ms, average_memory_usage_kb) where
    average_time_ms is the average execution time in milliseconds
    and average_memory_usage_kb is the average memory usage in kilobytes.
    """

    times = []
    memory_usages = []

    for _ in range(num_iterations):
        # Collect garbage to ensure memory stats are accurate
        gc.collect()

        # Measure initial values
        initial_memory = gc.mem_free()
        start_time = time.ticks_us()

        # Execute the function
        func(*args)

        # Measure end values
        end_time = time.ticks_us()
        final_memory = gc.mem_free()

        # Calculate time and memory usage for this iteration
        elapsed_time = time.ticks_diff(end_time, start_time) / 1000
        memory_usage = (initial_memory - final_memory) / 1024

        # Store the results
        times.append(elapsed_time)
        memory_usages.append(memory_usage)

    # Calculate the values
    average_time = sum(times) / num_iterations
    median_time = times[num_iterations // 2]
    average_memory_usage = sum(memory_usages) / num_iterations

    return average_time, median_time, average_memory_usage


def compare_functions(iters: int, funcs: list, *args):
    """
    Compares the performance of two functions and prints the results in a table format.

    :param iters: Number of iterations for performance measurement.
    :param func1: The first function to measure.
    :param func2: The second function to measure.
    :param args: Arguments to pass to the functions.
    """

    print()
    print(f"Running comparison for {len(funcs)} functions".center(80))

    avg = []
    med = []
    mem = []

    # Measure performance for func
    for func in funcs:
        avg_, med_, mem_ = measure_perf_per_iter(iters, func, *args)
        avg.append(avg_)
        med.append(med_)
        mem.append(mem_)

    print("#" * 80)

    print(f"{'Function':<20} {'Mean time (ms)':<20} {'Median time (ms)':<20} {'Mean Mem (KB)'}")
    print("="*80)

    # Print the results
    for i, func in enumerate(funcs):
        print(
            f"{func.__name__:<20} {avg[i]:<20.6f} {med[i]:<20.6f} {mem[i]:.6f}"
        )

    print("#" * 80, "\n")


# ------------------------------------------------------------------------------- #
# Functionally equivalent functions to compare
# ------------------------------------------------------------------------------- #


def function1(x, y, z):
    """ Example Version 1 of the function """
    weight1 = 0.5
    weight2 = 0.3
    weight3 = 0.2
    return (x * weight1) + (y * weight2) + (z * weight3)


def function2(x, y, z):
    """ Example Version 2 of the function """
    weights = [0.5, 0.3, 0.2]
    values = [x, y, z]
    return sum(val * weight for val, weight in zip(values, weights))


# ------------------------------------------------------------------------------- #
# Run the comparison for the functions when imported
# ------------------------------------------------------------------------------- #


# Arguments for the functions
x, y, z = 100, 200, 300

# Function to compare
functions = [function1, function2]

# Configure Device (Examples below)
# pyb.freq(120000000)  # Set the CPU frequency to 120MHz
# gc.threshold(1024)  # Set the garbage collection threshold
# .........

# Compare the two example functions for 1000 iterations
compare_functions(1000, functions, x, y, z)
