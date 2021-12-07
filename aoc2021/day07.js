const reader = require('./reader');
const fname = 'day07.in';

const part1 = async () => {
    const input = await reader.getContents(fname);
    const positions = input[0].split(",").map(Number);

    // Optimal position is median
    const sortedPositions = [...positions].sort((a, b) => a - b);
    const median = sortedPositions[Math.floor(sortedPositions.length / 2)];

    // Find sum of distances to median
    return positions.reduce((x, y) => x + Math.abs(y - median), 0);
}

const part2 = async () => {
    const input = await reader.getContents(fname);
    const positions = input[0].split(",").map(Number);

    // Optimal position is mean (2 possible means)
    const lowerMean = Math.floor(positions.reduce((x, y) => x + y, 0) / positions.length);
    const upperMean = Math.ceil(positions.reduce((x, y) => x + y, 0) / positions.length);

    // Find sum of distances to mean 
    return Math.min(positions.reduce((x, y) => x + Math.abs(y - lowerMean) * (Math.abs(y - lowerMean) + 1) / 2, 0),
            positions.reduce((x, y) => x + Math.abs(y - upperMean) * (Math.abs(y - upperMean) + 1) / 2, 0));
}

part1().then(console.log);
part2().then(console.log);
