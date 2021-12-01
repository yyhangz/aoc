const reader = require('./reader');
const fname = 'day01.in';

const part1 = async () => {
    const input = await reader.getContents(fname);
    let result = 0;
    let prevNum = Number.MAX_VALUE;

    for (const line of input) {
        if (Number(line) > prevNum) {
            result++;
        }

        prevNum = Number(line);
    }
    
    return result;
}

const part2 = async () => {
    const input = await reader.getContents(fname);
    let result = 0;

    for (let i = 0; i < input.length - 4; i++) {
        const currWindow = Number(input[i]);
        const nextWindow = Number(input[i + 3]);

        if (nextWindow > currWindow) {
            result++;
        }
   }

   return result;
}

part1().then(result => console.log(result));
part2().then(result => console.log(result));
