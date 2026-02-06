#!/usr/bin/env python3
# pylint: disable=invalid-name
"""
wordCount.py

Reads one text file or a directory containing multiple text files
and computes the frequency of each distinct word using
basic algorithms only.
Results are printed on screen and saved to WordCountResults.txt.
"""
# pylint: disable=invalid-name
import sys
import time
import os


def read_words_from_file(file_path):
    """
    Reads words from a single file.
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
    except Exception as error:
        print(f"Error reading file {file_path}: {error}")

    return words


def read_words_from_path(path):
    """
    Reads words from a file or all .txt files in a directory.
    """
    all_words = []

    if os.path.isfile(path):
        all_words.extend(read_words_from_file(path))

    elif os.path.isdir(path):
        for filename in os.listdir(path):
            if filename.lower().endswith(".txt"):
                file_path = os.path.join(path, filename)
                all_words.extend(read_words_from_file(file_path))
    else:
        print(f"Error: '{path}' is not a valid file or directory.")
        sys.exit(1)

    return all_words


def count_words(words):
    """
    Counts word frequencies using a basic algorithm.
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
        print("Usage: python wordCount.py <file_or_directory>")
        sys.exit(1)

    path = sys.argv[1]
    start_time = time.time()

    words = read_words_from_path(path)

    if not words:
        print("No valid words found.")
        sys.exit(1)

    frequencies = count_words(words)

    results = []
    for word, count in frequencies.items():
        results.append(f"Word: '{word}' | Frequency: {count}")

    elapsed_time = time.time() - start_time
    results.append(f"Execution Time (seconds): {elapsed_time}")

    for line in results:
        print(line)

    write_results(results)


if __name__ == "__main__":
    main()

