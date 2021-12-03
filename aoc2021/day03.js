const reader = require('./reader');
const fname = 'day03.in';

const part1 = async () => {
    const input = await reader.getContents(fname);
    let gamma = "";
    let epsilon = "";
    
    for (let i = 0; i < input[0].length; i++) {
        let zeroCount = 0;
        for (const line of input) {
            zeroCount += line[i] === "0" ? 1 : 0;
        }

        if (zeroCount > input.length - zeroCount) {
            gamma += "0";
            epsilon += "1";
        } else {
            gamma += "1";
            epsilon += "0";
        }
    }

    return parseInt(gamma, 2) * parseInt(epsilon, 2);
}

const part2 = async () => {
    const input = await reader.getContents(fname);

    let oxygen = [...input];
    let co2 = [...input];
    
    // Find oxygen
    for (let i = 0; i < input[0].length; i++) {
        if (oxygen.length === 1) {
            break;
        }

        let ones = [];
        let zeroes = [];

        for (const line of oxygen) {
            if (line[i] === "1") {
                ones.push(line);
            } else {
                zeroes.push(line);
            }
        }

        if (ones.length >= zeroes.length) {
            oxygen = [...ones];
        } else {
            oxygen = [...zeroes];
        }
    }

    // Find co2
    for (let i = 0; i < input[0].length; i++) {
        if (co2.length === 1) {
            break;
        }

        let ones = [];
        let zeroes = [];

        for (const line of co2) {
            if (line[i] === "1") {
                ones.push(line);
            } else {
                zeroes.push(line);
            }
        }

        if (zeroes.length <= ones.length) {
            co2 = [...zeroes];
        } else {
            co2 = [...ones];
        }
    }

    return parseInt(oxygen[0], 2) * parseInt(co2[0], 2);
}

part1().then(console.log);
part2().then(console.log);
