package day01

import (
	"errors"
	"strconv"
)

type intParser func(int, string) (int, error)

func GetLineNumber(line string, parse intParser) int {
	left, right, tens, ones := 0, len(line)-1, -1, -1
	for left <= right {
		if val, err := parse(left, line); tens < 0 && err == nil {
			tens = int(val)
		} else if tens < 0 {
			left++
		}

		if val, err := parse(right, line); ones < 0 && err == nil {
			ones = int(val)
		} else if ones < 0 {
			right--
		}

		if !(ones < 0 || tens < 0) {
			break
		}
	}
	return 10*tens + ones
}

func Part01(lines []string) int {
	sum := 0
	for _, line := range lines {
		sum += GetLineNumber(line, func(idx int, s string) (int, error) {
			val, err := strconv.ParseInt(string(s[idx]), 10, 64)
			return int(val), err
		})
	}
	return sum
}

func parseSymbol(c string) []string {
	m := map[string][]string{"o": []string{"one"},
		"t": []string{"two", "three"},
		"f": []string{"four", "five"},
		"s": []string{"six", "seven"},
		"e": []string{"eight"},
		"n": []string{"nine"},
	}

	return m[c]
}

func getWordNumeric(c string) int {
	m := map[string]int{"one": 1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
	}

	return m[c]
}

func parseIntOrWord(idx int, s string) (int, error) {
	val, err := strconv.ParseInt(string(s[idx]), 10, 64)
	if err == nil {
		return int(val), err
	} else {
		c := string(s[idx])
		possible_matches := parseSymbol(c)
		for _, match := range possible_matches {
			if len(match)+idx-1 < len(s) && s[idx:idx+len(match)] == match {
				return getWordNumeric(match), nil
			}
		}
	}
	return -1, errors.New("No matching characters")
}

func Part02(lines []string) int {
	sum := 0
	for _, line := range lines {
		sum += GetLineNumber(line, parseIntOrWord)
	}
	return sum
}
