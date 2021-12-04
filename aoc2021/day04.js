const reader = require('./reader');
const fname = 'day04.in';

const getDetails = (raw) => {
    const pulls = raw[0].trim().split(",").map(x => Number(x));
    const boards = [];

    for (let i = 1; i < raw.length; i++) {
        if (i + 1 < raw.length && !raw[i]) {
            const board = [];
            for (let d = 1; d <= 5; d++) {
                const line = [];
                for (const item of raw[i + d].trim().split(" ")) {
                    if (item) {
                        line.push({"value": Number(item), "isFilled": false});
                    }
                }
                board.push(line); 
            }
            boards.push(board);
        }
    }

    return {"pulls": pulls, "boards": boards};
}

const isWon = (board) => {
    // Check horizontal
    for (let i = 0; i < 5; i++) {
        let lineCount = 0;
        for (let j = 0; j < 5; j++) {
            lineCount += board[i][j].isFilled ? 1 : 0;
        }

        if (lineCount === 5) {
            return true;
        }
    }

    // Check vertical
    for (let j = 0; j < 5; j++) {
        let lineCount = 0;
        for (let i = 0; i < 5; i++) {
            lineCount += board[i][j].isFilled ? 1 : 0;
        }

        if (lineCount === 5) {
            return true;
        }
    }

    return false;
}

const getUnfilled = (board) => {
    const results = [];
    for (const line of board) {
        for (const item of line) {
            if (!item.isFilled) {
                results.push(item.value);
            }
        }
    }

    return results;
}

const part1 = async () => {
    const input = await reader.getContents(fname);
    const {pulls, boards} = getDetails(input);

    for (const currDraw of pulls) {
        // Fill boards
        for (const board of boards) {
            for (const line of board) {
                for (const item of line) {
                    if (item.value === currDraw) {
                        item.isFilled = true;
                    }
                }
            }
        }

        // Check for winning boards
        for (const board of boards) {
            if (isWon(board)) {
                return getUnfilled(board).reduce((x, y) => x + y, 0) * currDraw;
            }
        }
    }
}

const part2 = async () => {
    const input = await reader.getContents(fname);
    const {pulls, boards} = getDetails(input);
    // gives a list of [board index, score]
    const winList = [];

    for (const currDraw of pulls) {
        // Fill boards
        for (const board of boards) {
            for (const line of board) {
                for (const item of line) {
                    if (item.value === currDraw) {
                        item.isFilled = true;
                    }
                }
            }
        }

        // Check for winning boards
        for (const [idx, board] of boards.entries()) {
            if (winList.filter(entry => entry[0] === idx).length > 0) {
                continue;
            }

            if (isWon(board)) {
                const score = getUnfilled(board).reduce((x, y) => x + y, 0) * currDraw;
                winList.push([idx, score]);
            }
        }
    }

    return winList.pop()[1];
}

part1().then(console.log);
part2().then(console.log);
