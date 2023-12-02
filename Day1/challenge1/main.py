import time

import regex as re


def readInputFile(fileName):
    with open(fileName) as f:
        lines = f.readlines()
    return lines


with open("Day1/challenge1/input.txt", "r") as f:
    inputlines = f.read().splitlines()


def part1():
    start_time = time.time()
    ans = 0
    for line in inputlines:
        numline = []
        for char in line:
            if char.isdigit():
                numline.append(int(char))
        # print(numline[-1])
        ans += int(f"{numline[0]}{numline[-1]}")

    end_time = time.time()

    print(
        f"Sum of all digits in file is: {ans}, took {format((end_time - start_time) * 1000, ".3f")} milliseconds"
    )


def part2():
    start_time = time.time()

    wordstonum = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    def num(x: str):
        if x.isdigit():
            return x
        return wordstonum[x]

    pattern = "(?=(" + "|".join(wordstonum.keys()) + "|\\d))"
    ans = 0

    for line in inputlines:
        digits = re.findall(pattern, line)
        digits = [*map(num, digits)]
        ans += int(f"{digits[0]}{digits[-1]}")

    end_time = time.time()

    print(
        f"Sum of all numbers in file is: {ans}, took {format((end_time - start_time) * 1000, ".3f")} milliseconds"
    )


part1()
part2()

# below is my old code, this did not work


# for line in readInputFile("Day1/challenge1/input.txt"):
#     firstNumber = None
#     lastNumber = None
#     i = 0
#     while i < len(line):
#         if line[i].isdigit():
#             if firstNumber is None:
#                 firstNumber = int(line[i])
#             lastNumber = int(line[i])
#             i += 1
#         else:
#             for number in number_dict:
#                 if line[i:].startswith(number):
#                     # Check if the whole number word is present
#                     for j in range(len(number)):
#                         if i + j >= len(line) or line[i + j] != number[j]:
#                             break
#                     else:
#                         # If the whole number word is present, set firstNumber and lastNumber
#                         if firstNumber is None:
#                             firstNumber = number_dict[number]
#                         lastNumber = number_dict[number]
#                         i += len(number)
#                         break
#             else:
#                 i += 1

#     # Reverse logic for last number
#     i = len(line) - 1
#     while i >= 0:
#         if line[i].isdigit():
#             lastNumber = int(line[i])
#             i -= 1
#         else:
#             for number in reversed(number_dict.keys()):
#                 word_len = len(number)
#                 if (
#                     i - word_len + 1 >= 0
#                     and line[i - word_len + 1 : i + 1] == number
#                 ):
#                     # Check if the whole number word is present
#                     for j in range(word_len):
#                         if line[i - j] != number[-j - 1]:
#                             break
#                     else:
#                         # If the whole number word is present, set lastNumber
#                         lastNumber = number_dict[number]
#                         i -= word_len
#                         break
#             else:
#                 i -= 1
#     print("firstNumber is:", firstNumber)
#     print("lastNumber is:", lastNumber)
#     print("line is:", line)

#     try:
#         sum += (firstNumber * 10) + lastNumber
#     except TypeError:
#         print("firstNumber is:", firstNumber)
#         print("lastNumber is:", lastNumber)
#         print("line is:", line)
