"""
#!/usr/bin/env python3

computeStatistics.py

Computes descriptive statistics (mean, median, mode,
variance, standard deviation) from a file containing numbers.

"""

import sys
import time


def read_numbers_from_file(file_path):
    """
    Reads numbers from a file.
    Invalid data is reported and skipped.
    """
    numbers = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                value = line.strip()
                if not value:
                    continue
                try:
                    numbers.append(float(value))
                except ValueError:
                    print(
                        f"Invalid data at line {line_number}: '{value}'"
                    )
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    return numbers


def compute_mean(data):
    """calculate the mean of the numbers."""
    total = 0.0
    for value in data:
        total += value
    return total / len(data)


def compute_median(data):
    """calculate the median of the numbers"""
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]

def compute_mode(data):
    """calculate the mode of the numbers"""
    frequency = {}
    for value in data:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    max_count = max(frequency.values())
    modes = [k for k, v in frequency.items() if v == max_count]

    if len(modes) == len(frequency):
        return None

    return modes


def compute_variance(data, mean):
    """calculate the variance of the numbers"""
    total = 0.0
    for value in data:
        total += (value - mean) ** 2
    return total / len(data)


def compute_standard_deviation(variance):
    """calculate the standard deviation of the numbers"""
    return variance ** 0.5


def write_results(results):
    """write the result on StatisticsResults.txt."""
    with open("StatisticsResults.txt", "w", encoding="utf-8") as file:
        for line in results:
            file.write(line + "\n")


def main():
    """defination of the main"""
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py P1_TC1.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    data = read_numbers_from_file(file_path)

    if not data:
        print("No valid numeric data found.")
        sys.exit(1)

    mean = compute_mean(data)
    median = compute_median(data)
    mode = compute_mode(data)
    variance = compute_variance(data, mean)
    std_dev = compute_standard_deviation(variance)

    elapsed_time = time.time() - start_time

    results = [
        f"Count: {len(data)}",
        f"Mean: {mean}",
        f"Median: {median}",
        f"Mode: {mode}",
        f"Variance: {variance}",
        f"Standard Deviation: {std_dev}",
        f"Execution Time (seconds): {elapsed_time}"
    ]

    for line in results:
        print(line)

    write_results(results)


if __name__ == "__main__":
    main()
