package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	data, err := ioutil.ReadFile("input.txt")
	if err != nil {
		fmt.Println("File reading error", err)
		return
	}
	
	// Convert the input data to a string
	input := string(data)
	
	// Split the input string into lines
	lines := strings.Split(input, "\n")
	
	// TODO: Add the code to solve the challenge using the lines of input data
}