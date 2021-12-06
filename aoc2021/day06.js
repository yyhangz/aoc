const reader = require('./reader');
const fname = 'day06.in';

const toKey = (internalTimer, daysToEnd) => {
    return daysToEnd * 10 + internalTimer;
}

const getFamilySize = (internalTimer, daysToEnd, memoizer) => {
    const memoKey = toKey(internalTimer, daysToEnd);
    if (memoizer && memoizer[memoKey]) {
        return memoizer[memoKey];
    }

    let result;

    if (daysToEnd === 0) {
        result = 1;
    } else if (internalTimer === 0) {
        result = getFamilySize(6, daysToEnd - 1, memoizer) + getFamilySize(8, daysToEnd - 1, memoizer);
    } else {
        result = getFamilySize(internalTimer - 1, daysToEnd - 1, memoizer);
    }

    memoizer[memoKey] = result;
    return result;
}


const part1 = async () => {
    const input = await reader.getContents(fname);
    const memoizer = {};
    return input[0].split(",").map(Number).reduce((x, y) => x + getFamilySize(y, 80, memoizer), 0);
}

const part2 = async () => {
    const input = await reader.getContents(fname);
    const memoizer = {};
    return input[0].split(",").map(Number).reduce((x, y) => x + getFamilySize(y, 256, memoizer), 0);
}

part1().then(console.log);
part2().then(console.log);
