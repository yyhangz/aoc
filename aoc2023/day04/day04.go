package day04

import (
    "math"
    "strconv"
    "strings"
)

func getNums(nums []int) map[int]bool {
    res := make(map[int]bool)
    for _, num := range nums {
        res[num] = true
    }

    return res
}

func parseLine(line string) (winNums map[int]bool, yourNums map[int]bool) {
    lineSuffix := strings.Split(line, ": ")[1]
    numStrs := strings.Split(lineSuffix, " | ")
    winNums = getNums(parseNums(numStrs[0]))
    yourNums = getNums(parseNums(numStrs[1]))

    return winNums, yourNums
}

func parseNums(line string) []int {
    res := make([]int, 0)

    for _, numStr := range strings.Split(line, " ") {
        num, err := strconv.Atoi(numStr)
        if err == nil {
            res = append(res, num)
        }
    }

    return res
}

func powInt(x, y int) int {
    return int(math.Pow(float64(x), float64(y)))
}

func getWinningNums(winSet map[int]bool, yourSet map[int]bool) (winNums []int) {
    res := make([]int, 0)
    for num := range winSet {
        if yourSet[num] {
            res = append(res, num)
        }
    }

    return res
}

func computePart01LineScore(line string) int {
    winSet, yourSet := parseLine(line)
    winNums := getWinningNums(winSet, yourSet)

    res := 0
    if len(winNums) != 0 {
        res += powInt(2, len(winNums)-1)
    }

    return res
}

func computePart02(cardMap map[int]int, idx int, line string) map[int]int {
    winSet, yourSet := parseLine(line)
    winCount := len(getWinningNums(winSet, yourSet))
    for i := 0; i < winCount; i++ {
        cardMap[idx+i+1] += cardMap[idx]
    }

    return cardMap
}

func Part01(lines []string) int {
    res := 0
    for _, line := range lines {
        res += computePart01LineScore(line)
    }

    return res
}

func Part02(lines []string) int {
    var cardMap map[int]int = make(map[int]int)
    // Initialise each card to 1 count
    for idx, _ := range lines {
        cardMap[idx] = 1
    }

    for idx, line := range lines {
        cardMap = computePart02(cardMap, idx, line)
    }

    res := 0
    for _, num := range cardMap {
        res += num
    }

    return res
}
