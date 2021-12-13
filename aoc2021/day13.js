const reader = require('./reader');
const fname = 'day13.in';

const toKey = (x, y) => x + "," + y;
const toCoord = key => key.split(",").map(Number);

const parseInput = input => {
    const result = {"xLength": 0, "yLength": 0, "dots": new Set(), "instructions": []};

    // Parse dots
    let counter = 0;
    let line = input[counter];
    while (line) {
        const [x, y] = toCoord(line);
        result.xLength = Math.max(result.xLength, x + 1);
        result.yLength = Math.max(result.yLength, y + 1);
        result.dots.add(line);
        line = input[++counter];
    }

    // Parse instructions
    line = input[++counter];
    while (line) {
        const [axis, value] = line.split("along ")[1].split("=");
        result.instructions.push([axis, value]);
        line = input[++counter];
    }

    return result;
}

const execute = (dots, instruction, xLength, yLength) => {
    const [axis, value] = instruction;
    const newDots = new Set();
    const [foldAxisIdx, foldAxisLength, newX, newY] = 
        axis === "x" 
        ? [0, xLength, Math.floor(xLength / 2), yLength]
        : [1, yLength, xLength, Math.floor(yLength / 2)];

    dots.forEach(key => {
        const coords = toCoord(key);
        coords[foldAxisIdx] = coords[foldAxisIdx] < value
            ? coords[foldAxisIdx]
            : foldAxisLength - 1 - coords[foldAxisIdx];
        newDots.add(toKey(coords[0], coords[1]));
    });
    

    return {"dots": newDots, "xLength": newX, "yLength": newY};
}

const part1 = async () => {
    const input = await reader.getContents(fname);
    let {xLength, yLength, dots, instructions} = parseInput(input);
    const result = execute(dots, instructions[0], xLength, yLength);
    return result.dots.size;
}

const part2 = async () => {
    const input = await reader.getContents(fname);
    let {xLength, yLength, dots, instructions} = parseInput(input);
    for (const instruction of instructions) {
        const result = execute(dots, instruction, xLength, yLength);
        dots = result.dots;
        xLength = result.xLength;
        yLength = result.yLength;
    }


    let strBuilder = [];
    for (let y = 0; y < yLength; y++) {
        for (let x = 0; x < xLength; x++) {
            strBuilder.push(dots.has(toKey(x, y)) ? "*" : " ");
        }
        strBuilder.push("\n");
    }

    return strBuilder.join("");
}

part1().then(console.log);
part2().then(console.log);
