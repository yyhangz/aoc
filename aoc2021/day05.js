const reader = require('./reader');
const fname = 'day05.in';

class Coord {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    toString() {
        return this.x + "," + this.y;
    }

    // returns a list of Coords covered by the line formed by this and otherCoord
    getLineCoords(otherCoord, isCountDiagonal = false) {
        const result = [];
        let lower;
        let upper;
        let dx;
        let dy;

        if (this.x === otherCoord.x) {
            lower = this.y < otherCoord.y ? this : otherCoord;
            upper = this.y > otherCoord.y ? this : otherCoord;

            for (let i = lower.y; i <= upper.y; i++) {
                result.push(new Coord(this.x, i));
            }
        } else if (this.y === otherCoord.y) {
            lower = this.x < otherCoord.x ? this : otherCoord;
            upper = this.x > otherCoord.x ? this : otherCoord;

            for (let i = lower.x; i <= upper.x; i++) {
                result.push(new Coord(i, this.y));
            }
        } else if (isCountDiagonal) {
            dx = this.x < otherCoord.x ? 1 : -1;
            dy = this.y < otherCoord.y ? 1 : -1;

            let [currX, currY] = [this.x, this.y];
            while(currX !== otherCoord.x && currY !== otherCoord.y) {
                result.push(new Coord(currX, currY));
                currX += dx;
                currY += dy;
            }
            result.push(otherCoord);
        }

        return result;
    }
}

// Returns a list of [start Coord, end Coord] denoting the start and end points
const parseLines = (input) => {
    const result = [];

    for (const line of input) {
        if (!line) {
            continue;
        }

        let [start, end] = line.trim().split(" -> ");
        start = start.split(",");
        start = new Coord(Number(start[0]), Number(start[1]));
        end = end.split(",");
        end = new Coord(Number(end[0]), Number(end[1]));

        result.push([start, end]);
    }

    return result;
}


const part1 = async () => {
    const input = await reader.getContents(fname);
    const lines = parseLines(input);
    const coordMap = {};
    let result = 0;

    for (const line of lines) {
        const [start, end] = line;

        start.getLineCoords(end).forEach(coord => {
            const key = coord.toString();
            if (!(key in coordMap)) {
                coordMap[key] = 1;
            } else {
                coordMap[key]++;
            }
        });
    }

    for (const [key, value] of Object.entries(coordMap)) {
        if (value > 1) {
            result++;
        }
    }

    return result;
}

const part2 = async () => {
    const input = await reader.getContents(fname);
    const lines = parseLines(input);
    const coordMap = {};
    let result = 0;

    for (const line of lines) {
        const [start, end] = line;

        start.getLineCoords(end, true).forEach(coord => {
            const key = coord.toString();
            if (!(key in coordMap)) {
                coordMap[key] = 1;
            } else {
                coordMap[key]++;
            }
        });
    }

    for (const [key, value] of Object.entries(coordMap)) {
        if (value > 1) {
            result++;
        }
    }

    return result;
}

part1().then(console.log);
part2().then(console.log);
