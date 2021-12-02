const reader = require('./reader');
const fname = 'day02.in';

const part1 = async () => {
    const input = await reader.getContents(fname);
    let pos = [0, 0];

    for (const line of input) {
        const [cmd, val] = line.trim().split(" ");
        const amt = Number(val);
        const [x, y] = pos;

        switch(cmd) {
            case "forward":
                pos = [x + amt, y];
                break;
            case "up":
                pos = [x, y - amt];
                break;
            case "down":
                pos = [x, y + amt];
                break;
        }
    }

    return pos[0] * pos[1];
}

const part2 = async () => {
    const input = await reader.getContents(fname);
    let pos = [0, 0, 0];

    for (const line of input) {
        const [cmd, val] = line.trim().split(" ");
        const amt = Number(val);
        const [x, y, aim] = pos;

        switch(cmd) {
            case "forward":
                pos = [x + amt, y + (aim * amt), aim];
                break;
            case "up":
                pos = [x, y, aim - amt];
                break;
            case "down":
                pos = [x, y, aim + amt];
                break;
        }
    }

    return pos[0] * pos[1];
}

part1().then(console.log);
part2().then(console.log);
