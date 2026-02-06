#!/usr/bin/env python3
"""
convertNumbers.py

Reads a file or a directory containing text files with numbers.
Converts each valid number to binary and hexadecimal using
basic algorithms only.
Results are printed on screen and saved to ConvertionResults.txt.
"""
# pylint: disable=invalid-name
import sys
import time
import os


def read_numbers_from_file(file_path):
    """
    Reads integers from a single file.
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
                    numbers.append(int(value))
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


def convert_to_binary(number):
    """
    Converts an integer to binary using basic division algorithm.
    """
    if number == 0:
        return "0"

    is_negative = number < 0
    number = abs(number)
    result = ""

    while number > 0:
        result = str(number % 2) + result
        number //= 2

    if is_negative:
        result = "-" + result

    return result


def convert_to_hexadecimal(number):
    """
    Converts an integer to hexadecimal using basic division algorithm.
    """
    if number == 0:
        return "0"

    hex_symbols = "0123456789ABCDEF"
    is_negative = number < 0
    number = abs(number)
    result = ""

    while number > 0:
        remainder = number % 16
        result = hex_symbols[remainder] + result
        number //= 16

    if is_negative:
        result = "-" + result

    return result


def write_results(results):
    """
    Writes conversion results to ConvertionResults.txt.
    """
    with open("ConvertionResults.txt", "w", encoding="utf-8") as file:
        for line in results:
            file.write(line + "\n")


def main():
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py <file_or_directory>")
        sys.exit(1)

    path = sys.argv[1]
    start_time = time.time()

    numbers = read_numbers_from_path(path)
    results = []

    for number in numbers:
        binary = convert_to_binary(number)
        hexadecimal = convert_to_hexadecimal(number)

        results.append(
            f"Decimal: {number} | "
            f"Binary: {binary} | "
            f"Hexadecimal: {hexadecimal}"
        )

    elapsed_time = time.time() - start_time
    results.append(f"Execution Time (seconds): {elapsed_time}")

    for line in results:
        print(line)

    write_results(results)


if __name__ == "__main__":
    main()
