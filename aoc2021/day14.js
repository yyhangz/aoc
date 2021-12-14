const reader = require('./reader');
const fname = 'day14.in';

const parseInput = input => {
    const result = {"initial": input[0], "polyMap": {}};

    for (let i = 2; input[i]; i++) {
        const line = input[i];
        const [from, to] = line.split(" -> ");
        result.polyMap[from] = to;
    }

    return result;
}

const run = (pairsCount, polyMap) => {
    const result = {};
    for (const [key, value] of Object.entries(pairsCount)) {
        const generated = polyMap[key];
        const newPair1 = key[0] + generated;
        const newPair2 = generated + key[1];

        if (!result[newPair1]) {
            result[newPair1] = 0;
        }

        if (!result[newPair2]) {
            result[newPair2] = 0;
        }
        result[newPair1] += value;
        result[newPair2] += value;
    }
    return result;
}

const parsePairsCount = str => {
    const result = {};
    for (let i = 1; i < str.length; i++) {
        const key = str[i - 1] + str[i];
        if (!result[key]) {
            result[key] = 0;
        }
        result[key]++;
    }

    return result;
}

const findDiff = (pairsCount, start, end) => {
    const result = {};
    for (const [key, value] of Object.entries(pairsCount)) {
        if (!result[key[0]]) {
            result[key[0]] = 0;
        }

        if (!result[key[1]]) {
            result[key[1]] = 0;
        }
        result[key[0]] += value;
        result[key[1]] += value;
    }

    // Account for double counting of every character other than start and end
    result[start] += 1;
    result[end] += 1;
    let [min, max] = [Number.POSITIVE_INFINITY, 0]

    for (const [key, value] of Object.entries(result)) {
        result[key] /= 2;
        min = Math.min(result[key], min);
        max = Math.max(result[key], max);
    }

    return max - min;
}

const part1 = async () => {
    const input = await reader.getContents(fname);
    const {initial, polyMap} = parseInput(input);

    let pairs = parsePairsCount(initial);
    for (let i = 0; i < 10; i++) {
        pairs = run(pairs, polyMap);
    }

    return findDiff(pairs, initial[0], initial[initial.length - 1]);

}

const part2 = async () => {
    const input = await reader.getContents(fname);
    const {initial, polyMap} = parseInput(input);

    let pairs = parsePairsCount(initial);
    for (let i = 0; i < 40; i++) {
        pairs = run(pairs, polyMap);
    }

    return findDiff(pairs, initial[0], initial[initial.length - 1]);
}

part1().then(console.log);
part2().then(console.log);
