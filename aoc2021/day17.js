const reader = require('./reader');
const fname = 'day17.in';

const xSum = x => x * (x + 1) / 2;
const parseRanges = line => {
    const [a, b, xRaw, yRaw] = line.split(" ");
    const xRanges = xRaw.substring(2, xRaw.length - 1).split("..").map(Number);
    const yRanges = yRaw.substring(2).split("..").map(Number);
    return {"minX": xRanges[0], "maxX": xRanges[1], "minY": yRanges[0], "maxY": yRanges[1]};
}

const findXs = (min, max) => {
    const result = [];
    let curr = max;
    while (xSum(curr) >= min) {
        result.push(curr);
        curr--;
    }
    return result;
}

const isInTarget = (x, y, target) => {
    const {minX, maxX, minY, maxY} = target;
    let [xPos, yPos] = [0, 0];
    while (true) {
        if (xPos >= minX && xPos <= maxX && yPos >= minY && yPos <= maxY) {
            return true;
        }
        else if (xPos > maxX || yPos < minY) {
            return false;
        }
        xPos += x;
        yPos += y;
        x = x === 0 ? 0 : x - 1;
        y -= 1;
    }
}


const findMaxElevation = (x, target) => {
    let y = target.minY;
    let max = 0
    while (y <= Math.abs(target.minY)) {
        const isHit = isInTarget(x, y, target);
        if (isHit) {
            max = y;
        }
        y++;
    }
    return xSum(max);
}

const countPossibleVelocities = (x, target) => {
    let y = target.minY;
    let count = 0
    while (y <= Math.abs(target.minY) * 2) {
        const isHit = isInTarget(x, y, target);
        count += isHit ? 1 : 0;
        y++;
    }
    return count;
}


const part1 = async () => {
    const input = await reader.getContents(fname);
    const target = parseRanges(input[0]);
    const potentialXs = findXs(target.minX, target.maxX);
    return Math.max(...potentialXs.map(x => findMaxElevation(x, target)));
        
}

const part2 = async () => {
    const input = await reader.getContents(fname);
    const target = parseRanges(input[0]);
    const potentialXs = findXs(target.minX, target.maxX);
    return potentialXs.map(x => countPossibleVelocities(x, target)).reduce((a, b) => a + b, 0);
}

part1().then(console.log);
part2().then(console.log);
