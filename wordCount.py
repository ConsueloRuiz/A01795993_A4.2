"""
#!/usr/bin/env python3

wordCount.py

Reads a file containing words separated by spaces and
computes the frequency of each distinct word using
basic algorithms only (no special libraries).
Results are printed on screen and saved to
WordCountResults.txt.
"""

import sys
import time


def read_words_from_file(file_path):
    """
    Reads words from a file.
    Invalid data is reported and skipped.
    """
    words = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue

                parts = line.split(" ")
                for part in parts:
                    word = part.strip()
                    if word:
                        words.append(word)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    return words


def count_words(words):
    """
    Counts the frequency of each word using a basic algorithm.
    """
    frequencies = {}

    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    return frequencies


def write_results(results):
    """
    Writes results to WordCountResults.txt
    """
    with open("WordCountResults.txt", "w", encoding="utf-8") as file:
        for line in results:
            file.write(line + "\n")


def main():
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py P3_TC1.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    words = read_words_from_file(file_path)

    if not words:
        print("No valid words found in the file.")
        sys.exit(1)

    frequencies = count_words(words)

    results = []
    for word, count in frequencies.items():
        line = f"Word: '{word}' | Frequency: {count}"
        results.append(line)

    elapsed_time = time.time() - start_time
    time_line = f"Execution Time (seconds): {elapsed_time}"

    results.append(time_line)

    for line in results:
        print(line)

    write_results(results)


if __name__ == "__main__":
    main()

