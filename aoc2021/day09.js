const reader = require('./reader');
const fname = 'day09.in';

const dxdys = [[-1, 0], [0, 1], [1, 0], [0, -1]];

const toCoord = raw => {
    const result = [];
    raw.forEach(line => {
        if (line) {
            result.push(line.trim().split("").map(Number));
        }
    });
    return result;
}

const getRiskLevel = (x, y, smokeMap) => {
    const currLevel = smokeMap[x][y];

    for (const dxdy of dxdys) {
        const [dx, dy] = dxdy;
        const [newX, newY] = [x + dx, y + dy];
        if (newX >= 0 && newX < smokeMap.length && newY >= 0 && newY < smokeMap[0].length) {
            if (currLevel >= smokeMap[newX][newY]) {
                return 0;
            }
        }
    }

    return currLevel + 1;
}

const toKey = (x,y) => x * 1000 + y;
const toValue = key => [Math.floor(key / 1000), key % 1000]; 

// Returns the size of basin that includes the node in param using bfs
const bfs = (seen, nodeKey, smokeMap) => {
    let basinSize = 0;
    const bfsQueue = [nodeKey];

    while (bfsQueue.length > 0) {
        const key = bfsQueue.shift();
        const [currX, currY] = toValue(key);

        if (seen[key]) {
            continue;
        }

        seen[key] = true;
        basinSize++;
        for (const dxdy of dxdys) {
            const [dx, dy] = dxdy;
            const [newX, newY] = [currX + dx, currY + dy];

            if (newX >= 0 && newX < smokeMap.length && newY >= 0 && newY < smokeMap[0].length) {
                if (!seen[toKey(newX, newY)] && smokeMap[newX][newY] !== 9) {
                    bfsQueue.push(toKey(newX, newY));
                }
            }
        }
    }

    return basinSize;
}

const findBasins = smokeMap => {
    const seen = [];
    const result = [];

    // Initialize seen map
    for (let x = 0; x < smokeMap.length; x++) {
        for (let y = 0; y < smokeMap[0].length; y++) {
            seen[toKey(x, y)] = false;
        }
    }

    // Find list of basin sizes using bfs
    for (let x = 0; x < smokeMap.length; x++) {
        for (let y = 0; y < smokeMap[0].length; y++) {
            if (seen[toKey(x, y)] || smokeMap[x][y] === 9) {
                continue;
            }
            result.push(bfs(seen, toKey(x, y), smokeMap));
        }
    }
    return result;
}

const part1 = async () => {
    const input = await reader.getContents(fname);
    const smokeMap = toCoord(input);
    let result = 0;

    for (let x = 0; x < smokeMap.length; x++) {
        for (let y = 0; y < smokeMap[0].length; y++) {
            result += getRiskLevel(x, y, smokeMap);
        }
    }

    return result;
}

const part2 = async () => {
    const input = await reader.getContents(fname);
    const smokeMap = toCoord(input);

    const basins = findBasins(smokeMap).sort((a, b) => b - a);
    return basins[0] * basins[1] * basins[2]; 
}

part1().then(console.log);
part2().then(console.log);

