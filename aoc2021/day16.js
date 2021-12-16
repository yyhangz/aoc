const reader = require('./reader');
const fname = 'day16.in';

hexToBin = hex => hex.split("").map(x => parseInt(x, 16).toString(2).padStart(4, "0")).join("");
binToDec = bin => parseInt(bin, 2);

const parseLiteral = input => {
    const result = {};
    const literal = [];
    for (let i = 0; i < input.length; i += 5) {
        const block = input.substring(i, i + 5);
        literal.push(block.substring(1));
        if (block[0] === "0") {
            result.unused = input.substring(i + 5);
            break;
        }
    }
    result.value = binToDec(literal.join(""));
    return result;
}

const parseOperation = input => {
    const result = {"value": [], "unused": "", "parseLength": 0};
    switch (input[0]) {
        case "0": 
            let bitsParsed = 0;
            const bitLength = binToDec(input.substring(1, 16));
            let subPackets = input.substring(16);
            while (subPackets) {
                const data = parse(subPackets);
                bitsParsed += data.parseLength;
                result.value.push(data);
                subPackets = data.unused;
                if (bitsParsed === bitLength) {
                    break;
                }
            }
            result.unused = subPackets;
            result.parseLength = input.length - subPackets.length;
            break;
        default:
            const pacLength = binToDec(input.substring(1, 12));
            let remainder = input.substring(12);
            for (let i = 0; i < pacLength; i++) {
                const data = parse(remainder);
                result.value.push(data);
                remainder = data.unused;
            }
            result.unused = remainder;
            result.parseLength = input.length - remainder.length;
            break;
    }
    return result;
}

const parse = (input) => {
    const result = {};
    result.pacVer = binToDec(input.substring(0, 3));
    result.pacId = binToDec(input.substring(3, 6));
    const remainder = input.substring(6);

    let data;
    switch (result.pacId) {
        case 4:
            data = parseLiteral(remainder);
            break;
        default:
            data = parseOperation(remainder);
    }
    result.body = data.value;
    result.unused = data.unused;
    result.parseLength = input.length - result.unused.length;
    return result;
}

const sumVersions = result => {
    const internal = isNaN(result.body) ? result.body.map(sumVersions).reduce((a, b) => a + b, 0) : 0;
    return result.pacVer + internal; 
}

const findValue = result => {
    let data;
    switch (result.pacId) {
        case 4:
            return result.body;
            break;
        case 0:
            return result.body.map(findValue).reduce((a, b) => a + b, 0);
            break;
        case 1:
            return result.body.map(findValue).reduce((a, b) => a * b, 1);
            break;
        case 2:
            return Math.min(...result.body.map(findValue));
            break;
        case 3:
            return Math.max(...result.body.map(findValue));
            break;
        case 5:
            data = result.body.map(findValue);
            return data[0] > data[1] ? 1 : 0;
            break;
        case 6:
            data = result.body.map(findValue);
            return data[0] < data[1] ? 1 : 0;
            break;
        case 7:
            data = result.body.map(findValue);
            return data[0] === data[1] ? 1 : 0;
            break;
    }
}

const part1 = async () => {
    const input = await reader.getContents(fname);
    const binInput = hexToBin(input[0]);
    return sumVersions(parse(binInput));
}

const part2 = async () => {
    const input = await reader.getContents(fname);
    const binInput = hexToBin(input[0]);
    return findValue(parse(binInput));
}

part1().then(console.log);
part2().then(console.log);
