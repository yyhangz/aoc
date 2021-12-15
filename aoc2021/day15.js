const reader = require('./reader');
const fname = 'day15.in';

const directions = [[-1, 0], [0, 1], [1, 0], [0, -1]];
const toKey = (x, y) => x + "," + y;
const toCoord = key => key.split(",").map(Number);
const isValidKey = (key, rowLength, colLength) => {
    const [row, col] = toCoord(key);
    return row >= 0 && row < rowLength && col >= 0 && col < colLength;
};

const sssp = coords => {
    const visited = new Set();
    const pq = {};
    const endKey = toKey(coords.length - 1, coords[0].length - 1);

    // Initialize pq
    const key = toKey(0, 0);
    pq[key] = 0;

    // Dijkstra's
    while(visited.size !== coords.length * coords[0].length) {
        const [key, value] = Object.entries(pq).sort((a, b) => a[1] - b[1])[0];

        if (key === endKey) {
            return value;
        }

        const [row, col] = toCoord(key);
        visited.add(key);
        delete pq[key];

        for (const [dx, dy] of directions) {
            const neighbourKey = toKey(row + dx, col + dy);
            if (!visited.has(neighbourKey) && isValidKey(neighbourKey, coords.length, coords[0].length)) {
                const currDist = pq[neighbourKey] ? pq[neighbourKey] : Number.POSITIVE_INFINITY;
                pq[neighbourKey] = Math.min(currDist, value + coords[row + dx][col + dy]);
            }
        }
    }
}

const bigifyMap = coords => {
    const result = [];
    for (let row = 0; row < coords.length * 5; row++) {
        const line = [];
        for (let col = 0; col < coords[0].length * 5; col++) {
            const seedVal = coords[row % coords.length][col % coords[0].length];
            const incrementAmt = Math.floor(row / coords.length) + Math.floor(col / coords[0].length);
            let finalVal = seedVal;
            for (let i = 0; i < incrementAmt; i++) {
                finalVal++;
                if (finalVal > 9) {
                    finalVal = 1;
                }
            }
            line.push(finalVal);
        }
        result.push(line);
    }
    return result;
}

const part1 = async () => {
    const input = await reader.getContents(fname);
    const coords = [];
    input.forEach(line => {
        if (line) {
            coords.push(line.split("").map(Number));
        }
    });

    return sssp(coords);
}

const part2 = async () => {
    // Part 2 takes roughly 1 min to 4 mins to run depending on the hardware
    const input = await reader.getContents(fname);
    let coords = [];
    input.forEach(line => {
        if (line) {
            coords.push(line.split("").map(Number));
        }
    });
    coords = bigifyMap(coords);
    return sssp(coords);
}

part1().then(console.log);
part2().then(console.log);
