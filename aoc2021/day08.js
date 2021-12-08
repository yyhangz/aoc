const reader = require('./reader');
const fname = 'day08.in';

const numberMap = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'], // 6 nums
    1: ['c', 'f'], // 2 nums
    2: ['a', 'c', 'd', 'e', 'g'], // 5 nums
    3: ['a', 'c', 'd', 'f', 'g'], // 5 nums
    4: ['b', 'c', 'd', 'f'], // 4 nums
    5: ['a', 'b', 'd', 'f', 'g'], // 5 nums
    6: ['a', 'b', 'd', 'e', 'f', 'g'], // 6 nums
    7: ['a', 'c', 'f'], // 3 nums
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'], // 7 nums
    9: ['a', 'b', 'c', 'd', 'f', 'g'] // 6 nums
}

const getSignalList = str => str ? str.split(" | ")[0].split(" ") : [];
const getOutputList = str => str ? str.split(" | ")[1].split(" ") : [];

// Generate all permutations of an array
const generateAllPerm = arr => {
    function p(arr, temp) {
        var i, x;
        if (!arr.length) {
            result.push(temp);
        }
        for (i = 0; i < arr.length; i++) {
            x = arr.splice(i, 1)[0];
            p(arr, temp.concat(x));
            arr.splice(i, 0, x);
        }
    }

    const result = [];
    p(arr, []);
    return result;
}

const isValidMap = (possible, unsolvedSignals) => {
    let numMatches = -1;
    for (const [idx, unsolvedSignal] of unsolvedSignals.entries()) {
        const mappedSignal = unsolvedSignal.split("").map(x => possible[x]).sort();
        for (const [key, value] of Object.entries(numberMap)) {
            if (value.join("") === mappedSignal.join("")) {
                numMatches++;
                break;
            }
        }
        if (numMatches !== idx) {
            return false;
        }
    }
    return true;
}

const solve = (unsolvedOutput, decryptedMap) => {
    let result = "";
    for (const output of unsolvedOutput) {
        const correctOutput = output.split("").map(x => decryptedMap[x]).sort().join("");
        for (const [key, value] of Object.entries(numberMap)) {
            if (value.join("") === correctOutput) {
                result += key;
                break;
            }
        }
    }
    return result;
}

const part1 = async () => {
    const input = await reader.getContents(fname);
    return input.map(x => getOutputList(x).filter(y => y.length !== 5 && y.length !== 6))
        .reduce((x, y) => x + y.length, 0);
}

const part2 = async () => {
    const input = await reader.getContents(fname);
    const possibleMaps = generateAllPerm(['a', 'b', 'c', 'd', 'e', 'f', 'g']).map(x => {
        const result = {};
        const aCode = "a".charCodeAt(0);
        x.forEach((c, idx) => {
            result[c] = String.fromCharCode(aCode + idx);
        });
        return result;
    });
    let result = 0;
    let decryptedMap;

    for (const line of input) {
        const unsolvedSignal = getSignalList(line);
        const unsolvedOutput = getOutputList(line);

        for (const possible of possibleMaps) {
            if (isValidMap(possible, unsolvedSignal)) {
                decryptedMap = possible;
                break;
            }
        }

        result += Number(solve(unsolvedOutput, decryptedMap));
    }

    return result;
}

part1().then(console.log);
part2().then(console.log);
