const reader = require('./reader');
const fname = 'day11.in';

const directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]];

const toKey = (row, col) => row * 1000 + col;

const toVal = key => [Math.floor(key / 1000), key % 1000];

const incrementAll = octopuses => {
    for (let row = 0; row < octopuses.length; row++) {
        for (let col = 0; col < octopuses[0].length; col++) {
            octopuses[row][col]++;
        }
    }
}

const flashAll = octopuses => {
    const isFlashed = {};
    const flashQueue = [];

    // Find initial flashers
    for (let row = 0; row < octopuses.length; row++) {
        for (let col = 0; col < octopuses[0].length; col++) {
            if (octopuses[row][col] > 9) {
                flashQueue.push(toKey(row, col));
            }
        }
    }

    // Trigger domino effect of flashes
    while (flashQueue.length > 0) {
        const key = flashQueue.shift();
        const [row, col] = toVal(key);

        if (!isFlashed[key]) {
            isFlashed[key] = true;

            for (const [dRow, dCol] of directions) {
                const [newRow, newCol] = [row + dRow, col + dCol];
                if (newRow < 0 || newRow >= octopuses.length || newCol < 0 || newCol >= octopuses[0].length) {
                    continue;
                }

                const newVal = ++octopuses[newRow][newCol];
                if (newVal > 9 && !isFlashed[toKey(newRow, newCol)]) {
                    flashQueue.push(toKey(newRow, newCol));
                }
            }
        }
    }

    // Reset flashers and return count
    let counter = 0;
    for (const [key, val] of Object.entries(isFlashed)) {
        const [row, col] = toVal(key);
        octopuses[row][col] = 0;
        counter++;
    }

    return counter;
}

const part1 = async () => {
    const input = await reader.getContents(fname);
    const octopuses = [];
    for (const line of input) {
        if (line) {
            octopuses.push(line.split("").map(Number));
        }
    }

    let result = 0;
    for (let i = 0; i < 100; i++) {
        incrementAll(octopuses);
        result += flashAll(octopuses);
    }
    return result;
}

const part2 = async () => {
    const input = await reader.getContents(fname);
    const octopuses = [];
    for (const line of input) {
        if (line) {
            octopuses.push(line.split("").map(Number));
        }
    }

    let result = 0;
    while (true) {
        incrementAll(octopuses);
        const temp = flashAll(octopuses);
        result++;

        if (temp === octopuses.length * octopuses[0].length) {
            return result;
        }
    }
}

part1().then(console.log);
part2().then(console.log);
