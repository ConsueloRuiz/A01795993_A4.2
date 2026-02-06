#!/usr/bin/env python3
"""
computeStatistics.py

Reads a file or a directory containing text files with numbers
and computes descriptive statistics using basic algorithms only.
Results are printed on screen and saved to StatisticsResults.txt.
"""
# pylint: disable=invalid-name
import sys
import time
import os


def read_numbers_from_file(file_path):
    """
    Reads numeric values from a single file.
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
                        f"Invalid data in {file_path} "
                        f"at line {line_number}: '{value}'"
                    )
    except Exception as error:
        print(f"Error reading file {file_path}: {error}")

    return numbers


def read_numbers_from_path(path):
    """
    Reads numbers from a file or from all .txt files in a directory.
    """
    all_numbers = []

    if os.path.isfile(path):
        all_numbers.extend(read_numbers_from_file(path))

    elif os.path.isdir(path):
        for filename in os.listdir(path):
            if filename.lower().endswith(".txt"):
                file_path = os.path.join(path, filename)
                all_numbers.extend(read_numbers_from_file(file_path))
    else:
        print(f"Error: '{path}' is not a valid file or directory.")
        sys.exit(1)

    return all_numbers


def compute_mean(data):
    total = 0.0
    for value in data:
        total += value
    return total / len(data)


def compute_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2

    return sorted_data[mid]


def compute_mode(data):
    frequency = {}

    for value in data:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    max_count = 0
    mode_value = None
    multiple_modes = False

    for key in frequency:
        if frequency[key] > max_count:
            max_count = frequency[key]
            mode_value = key
            multiple_modes = False
        elif frequency[key] == max_count:
            multiple_modes = True

    if multiple_modes:
        return None

    return mode_value


def compute_variance(data, mean):
    total = 0.0
    for value in data:
        total += (value - mean) ** 2
    return total / len(data)


def compute_standard_deviation(variance):
    return variance ** 0.5


def write_results(results):
    """
    Writes results to StatisticsResults.txt.
    """
    with open("StatisticsResults.txt", "w", encoding="utf-8") as file:
        for line in results:
            file.write(line + "\n")


def main():
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py <file_or_directory>")
        sys.exit(1)

    path = sys.argv[1]
    start_time = time.time()

    data = read_numbers_from_path(path)

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
