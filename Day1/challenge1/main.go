package main

import (
	"fmt"
	"os"
	"strings"
)

// file path: Day1/challenge1/input.txt

func main() {
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

func contains(slice []int, val int) bool {
	for _, item := range slice {
		if item == val {
			return true
		}
	}
	return false
}
