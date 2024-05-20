package day03

import (
    "strconv"
)

type coords struct {
    row      int
    colStart int
    colEnd   int
}

type gearCoords struct {
    row int
    col int
}

const PERIOD = "."
const GEAR = "*"

func isNumeric(s string) bool {
    _, err := strconv.ParseInt(s, 10, 64)
    return err == nil
}

func findStrRanges(line string, row int) []coords {
    line = line + "."
    res := make([]coords, 0)
    isPrevNum := false
    currRange := coords{row, 0, 0}
    for i := 0; i < len(line); i++ {
        c := string(line[i])
        if isNumeric(c) && !isPrevNum {
            currRange.colStart = i
            isPrevNum = true
        } else if !isNumeric(c) && isPrevNum {
            currRange.colEnd = i - 1
            res = append(res, currRange)
            currRange = coords{row, currRange.colStart, currRange.colEnd}
            isPrevNum = false
        }
    }

    return res
}

func getBorderRange(c coords, maxRow int, maxCol int) (start coords, end coords) {
    startRow := 0
    if c.row == 0 {
        startRow = c.row
    } else {
        startRow = c.row - 1
    }
    startCol := 0
    if c.colStart == 0 {
        startCol = c.colStart
    } else {
        startCol = c.colStart - 1
    }

    endRow := c.row
    if c.row == maxRow {
        endRow = c.row
    } else {
        endRow = c.row + 1
    }
    endCol := c.colEnd
    if c.colEnd == maxCol {
        endCol = c.colEnd
    } else {
        endCol = c.colEnd + 1
    }
    start = coords{startRow, startCol, endCol}
    end = coords{endRow, startCol, endCol}

    return start, end
}

func containsSpecial(start coords, end coords, lines []string) bool {
    for i := start.row; i <= end.row; i++ {
        for j := start.colStart; j <= end.colEnd; j++ {
            char := string(lines[i][j])
            if !(char == PERIOD || isNumeric(char)) {
                return true
            }
        }
    }

    return false
}

func getNumFromCoord(c coords, lines []string) int {
    numStr := lines[c.row][c.colStart : c.colEnd+1]
    val, _ := strconv.ParseInt(numStr, 10, 64)
    return int(val)
}

func getBoundaryGears(start coords, end coords, lines []string) []gearCoords {
    res := make([]gearCoords, 0)
    for i := start.row; i <= end.row; i++ {
        for j := start.colStart; j <= end.colEnd; j++ {
            char := string(lines[i][j])
            if char == GEAR {
                res = append(res, gearCoords{i, j})
            }
        }
    }

    return res
}

func Part01(lines []string) int {
    res := 0
    for row, line := range lines {
        lineNums := findStrRanges(line, row)
        for _, lineNum := range lineNums {
            start, end := getBorderRange(lineNum, len(lines)-1, len(line)-1)
            if containsSpecial(start, end, lines) {
                res += getNumFromCoord(lineNum, lines)
            }
        }
    }

    return res
}

func Part02(lines []string) int {
    res := 0
    gearMap := map[gearCoords][]int{}
    for row, line := range lines {
        lineNums := findStrRanges(line, row)
        for _, lineNum := range lineNums {
            start, end := getBorderRange(lineNum, len(lines)-1, len(line)-1)
            gearLocs := getBoundaryGears(start, end, lines)
            val := getNumFromCoord(lineNum, lines)

            for _, gear := range gearLocs {
                if gearMap[gear] == nil {
                    gearMap[gear] = []int{val}
                } else {
                    gearMap[gear] = append(gearMap[gear], val)
                }
            }
        }
    }

    for _, intVals := range gearMap {
        if len(intVals) == 2 {
            res += intVals[0] * intVals[1]
        }
    }

    return res
}
