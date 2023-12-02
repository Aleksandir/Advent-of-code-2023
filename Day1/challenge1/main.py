import re
import time


def readInputFile(fileName):
    with open(fileName) as f:
        lines = f.readlines()
    return lines


def main():
    sum = 0

    start_time = time.time()

    for line in readInputFile("Day1/challenge1/input.txt"):
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for char in line:
            if char in digits:
                firstNumber = char
                break

        for char in reversed(line):
            if char in digits:
                secondNumber = char
                break
        sum += (int(firstNumber) * 10) + int(secondNumber)

    end_time = time.time()

    print("Sum of all numbers in file is:", sum)
    print("Execution time:", (end_time - start_time) * 1000, "milliseconds")


main()
