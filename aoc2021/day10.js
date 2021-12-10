const reader = require('./reader');
const fname = 'day10.in';

const closeMap = {
    '}': '{',
    ')': '(',
    ']': '[',
    '>': '<'
}

const scoreMap = {
    '}': 1197,
    ')': 3,
    ']': 57,
    '>': 25137 
}

const openMap = {
    '{': 3,
    '(': 1,
    '[': 2,
    '<': 4
}

const getCorruptedChar = line => {
    const stack = [];
    for (const c of line) {
        if (!closeMap[c]) {
            stack.push(c);
        } else {
            if (stack.pop() !== closeMap[c]) {
                return c;
            }
        }
    }

    return undefined;
}

const getAutoCompleteScore = line => {
    const stack = [];
    let result = 0;
    for (const c of line) {
        if (!closeMap[c]) {
            stack.push(c);
        } else {
            if (stack.pop() !== closeMap[c]) {
                return result;
            }
        }
    }

    while(stack.length > 0) {
        result *= 5;
        result += openMap[stack.pop()];
    }

    return result;
}

const part1 = async () => {
    const input = await reader.getContents(fname);
    let result = 0;

    input.forEach(line => {
        const val = getCorruptedChar(line);
        if (val) {
            result += scoreMap[val];
        }
    });

    return result;
}

const part2 = async () => {
    const input = await reader.getContents(fname);
    const results = [];

    for (const line of input) {
        const score = getAutoCompleteScore(line);
        if (score > 0) {
            results.push(score);
        }
    }

    results.sort((a,b) => a - b);
    return results[Math.floor(results.length / 2)];
}

part1().then(console.log);
part2().then(console.log);
