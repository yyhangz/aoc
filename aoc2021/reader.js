const fs = require('fs');
const readline = require('readline');

// Returns an array of stripped lines
const getContents = async (fileName) => {
    const fileStream = fs.createReadStream(fileName);
    const result = [];

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    for await (const line of rl) {
        result.push(line.trim());
    }
    return result;
}

exports.getContents = getContents;
