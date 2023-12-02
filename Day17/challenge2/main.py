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
	// The input data is converted to a string and split into lines.
	input := strings.Split(string(data), "\n")

	// TODO: Add the code to solve the challenge using the input data.
}