package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"
)

// sudo code for how to go through garbled text line and find hidden words in garbled string
// 1. go through each line in file
// 2. go through each character in line
// 3. init index to 0
// 3. if letter, for loop through slice of numbers as words
// 4. if letter match number, continue to next letter
// 5. if letter does not match number, break out of loop and continue to next letter

var numberDict = map[string]string{
	"one":   "1",
	"two":   "2",
	"three": "3",
	"four":  "4",
	"five":  "5",
	"six":   "6",
	"seven": "7",
	"eight": "8",
	"nine":  "9",
	"zero":  "0",
}

func main() {
	s := "four1sevenbfbnqvkbfoursix7"
	first, last := findFirstAndLastNumber(s)
	fmt.Printf("First number: %s, Last number: %s\n", first, last)
}

func main2() {
	var sum int = 0

	for _, line := range readInputFile("Day1/challenge1/input.txt") {
		var digits []int = []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

		// get first number in line
		var firstNumber int = 0
		for i := 0; i < len(line); i++ {
			if contains(digits, int(line[i]-'0')) {
				firstNumber = int(line[i] - '0')

				break
			}
		}

		// get second number in line
		var secondNumber int = 0
		for j := len(line) - 1; j >= 0; j-- {
			if contains(digits, int(line[j]-'0')) {
				secondNumber = int(line[j] - '0')
				break
			}

		}

		sum += (firstNumber * 10) + secondNumber

	}
	fmt.Println("Sum of all numbers in file is: ", sum)
}
func readInputFile(fileName string) []string {
	data, err := os.ReadFile(fileName)
	if err != nil {
		fmt.Println("File reading error", err)
		return nil
	}

	// Convert the input data to a string
	input := string(data)

	// Split the input string into lines
	lines := strings.Split(input, "\n")

	return lines
}

func findFirstAndLastNumber(s string) (string, string) {
	numbers := regexp.MustCompile(`\b(?:one|two|three|four|five|six|seven|eight|nine|zero|\d+)\b`).FindAllString(s, -1)
	for i, number := range numbers {
		numbers[i] = numberDict[number]
	}
	return numbers[0], numbers[len(numbers)-1]
}

func contains(slice []int, val int) bool {
	for _, item := range slice {
		if item == val {
			return true
		}
	}
	return false
}
