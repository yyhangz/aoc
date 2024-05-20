package main

import (
	day03 "aoc2023/day03"
	"bufio"
	"fmt"
	"os"
)

func getLines(fname string) []string {
	file, err := os.Open(fname)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return make([]string, 0)
	}
	defer file.Close()

	// Create a scanner to read the file line by line
	scanner := bufio.NewScanner(file)

	// Create a slice to store the lines
	var lines []string

	// Read lines until the end of the file
	for scanner.Scan() {
		// Append each line to the slice
		lines = append(lines, scanner.Text())
	}

	// Check for any errors during scanning
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return make([]string, 0)
	}

	return lines
}

func main() {
	content := getLines("./day03/day03.in")
	fmt.Println(day03.Part01(content))
	fmt.Println(day03.Part02(content))
}
