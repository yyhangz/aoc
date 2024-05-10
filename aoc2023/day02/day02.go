package day02

import (
	"strconv"
	"strings"
)

const RED_VAL, GREEN_VAL, BLUE_VAL = 12, 13, 14
const RED, GREEN, BLUE = "red", "green", "blue"

var COLOUR_LIST = []string{RED, GREEN, BLUE}
var COLOUR_MAP = map[string]int{RED: RED_VAL,
	GREEN: GREEN_VAL,
	BLUE:  BLUE_VAL,
}

func parseGame(game string) map[string]int {
	m := map[string]int{}

	for _, item := range strings.Split(game, ", ") {
		keyValuePair := strings.Split(item, " ")
		colour := keyValuePair[1]
		temp, _ := strconv.ParseInt(keyValuePair[0], 10, 64)
		value := int(temp)
		m[colour] = value
	}
	return m
}

func getGames(line string) (gameId int, games []map[string]int) {
	lineSplit := strings.Split(line, ": ")
	gameNumber, _ := strconv.ParseInt(strings.Split(lineSplit[0], "Game ")[1], 10, 64)
	gameId = int(gameNumber)

	gamesUnparsed := strings.Split(lineSplit[1], "; ")
	games = make([]map[string]int, 0)
	for _, g := range gamesUnparsed {
		games = append(games, parseGame(g))
	}
	return gameId, games
}

func isValid(matches []map[string]int) bool {
	for _, match := range matches {
		for _, colour := range COLOUR_LIST {
			if match[colour] > COLOUR_MAP[colour] {
				return false
			}
		}
	}
	return true
}

func Part01(lines []string) int {
	res := 0
	for _, line := range lines {
		gameId, games := getGames(line)
		if isValid(games) {
			res += gameId
		}
	}
	return res
}

func findPower(matches []map[string]int) int {
	minCounts := map[string]int{
		RED:   0,
		BLUE:  0,
		GREEN: 0,
	}
	for _, match := range matches {
		for _, colour := range COLOUR_LIST {
			minCounts[colour] = max(minCounts[colour], match[colour])
		}
	}
	return minCounts[RED] * minCounts[BLUE] * minCounts[GREEN]
}

func Part02(lines []string) int {
	res := 0
	for _, line := range lines {
		_, games := getGames(line)
		res += findPower(games)
	}
	return res
}
