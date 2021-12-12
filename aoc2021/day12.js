const reader = require('./reader');
const fname = 'day12.in';

class Node {
    constructor(name) {
        this.name = name;
        this.edges = [];
    }

    addEdge(node) {
        this.edges = [...this.edges, node];
    }

    isBig() {
        return this.name === this.name.toUpperCase();
    }

    isStart() {
        return this.name === "start";
    }

    isEnd() {
        return this.name ==="end";
    }
}

const createNodes = input => {
    const nodes = {};
    for (const line of input) {
        if (!line) {
            continue;
        }

        const [from, to] = line.split("-");
        const fromNode = nodes[from] ? nodes[from] : new Node(from);
        const toNode = nodes[to] ? nodes[to] : new Node(to);

        fromNode.addEdge(toNode);
        toNode.addEdge(fromNode);
        nodes[from] = fromNode;
        nodes[to] = toNode;
    }

    const result = [];
    for (const [name, node] of Object.entries(nodes)) {
        result.push(node);
    }
    return result;
}

const dfs = (node, visited, isDoubleVisited) => {
    if (node.isEnd()) {
        return 1;
    }

    if(visited.has(node) && (node.isStart() || isDoubleVisited)) {
        return 0;
    } 

    const useDoubleVisit = !isDoubleVisited && visited.has(node);
    const updatedVisited = new Set(visited);
    let result = 0;
    if (!node.isBig()) {
        updatedVisited.add(node);
    }

    for (const neighbour of node.edges) {
        if (useDoubleVisit) {
            result += dfs(neighbour, updatedVisited, true);
        } else {
            result += dfs(neighbour, updatedVisited, isDoubleVisited);
        }
    }


    return result;
}

const part1 = async () => {
    const input = await reader.getContents(fname);

    const nodes = createNodes(input);
    const start = nodes.filter(node => node.isStart())[0];
    return dfs(start, new Set(), true);
}

const part2 = async () => {
    const input = await reader.getContents(fname);

    const nodes = createNodes(input);
    const start = nodes.filter(node => node.isStart())[0];
    return dfs(start, new Set(), false);
}

part1().then(console.log);
part2().then(console.log);
