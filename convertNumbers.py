"""
#!/usr/bin/env python3

convertNumbers.py

Reads a file containing numbers and converts each valid number
to binary and hexadecimal using basic algorithms only.
Results are printed on screen and saved to ConvertionResults.txt.
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
                    numbers.append(int(value))
                except ValueError:
                    print(
                        f"Invalid data at line {line_number}: '{value}'"
                    )
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    return numbers


def to_binary(number):
    """
    Converts an integer to binary using basic division algorithm.
    """
    if number == 0:
        return "0"

    is_negative = number < 0
    number = abs(number)
    digits = ""

    while number > 0:
        digits = str(number % 2) + digits
        number //= 2

    if is_negative:
        digits = "-" + digits

    return digits


def to_hexadecimal(number):
    """
    Converts an integer to hexadecimal using basic division algorithm.
    """
    if number == 0:
        return "0"

    hex_digits = "0123456789ABCDEF"
    is_negative = number < 0
    number = abs(number)
    digits = ""

    while number > 0:
        remainder = number % 16
        digits = hex_digits[remainder] + digits
        number //= 16

    if is_negative:
        digits = "-" + digits

    return digits


def write_results(results):
    """
    Writes results to ConvertionResults.txt
    """
    with open("ConvertionResults.txt", "w", encoding="utf-8") as file:
        for line in results:
            file.write(line + "\n")


def main():
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py P2_TC1.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    numbers = read_numbers_from_file(file_path)

    results = []

    for number in numbers:
        binary = to_binary(number)
        hexadecimal = to_hexadecimal(number)
        line = (
            f"Decimal: {number} | "
            f"Binary: {binary} | "
            f"Hexadecimal: {hexadecimal}"
        )
        results.append(line)

    elapsed_time = time.time() - start_time
    time_line = f"Execution Time (seconds): {elapsed_time}"

    results.append(time_line)

    for line in results:
        print(line)

    write_results(results)


if __name__ == "__main__":
    main()

