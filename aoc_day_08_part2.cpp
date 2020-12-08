#include "aoc.hpp"
using namespace std;

int encode(string str) { // ones place: 0 for nop, 1 for acc, 2 for jmp, anything aft is arg value
    string inst = str.substr(0,3);
    int code = 0;
    if (inst == "acc") {
        code = 1;
    } else if (inst == "jmp") {
        code = 2;
    }
    code += stoi(str.substr(5)) * 10;
    code *= str[4] == '+' ? 1 : -1;
    return code;
}

void decode(int code, vector<int> & decoded) {
    decoded[0] = abs(code) % 10;
    decoded[1] = code / 10;
    return;
}

// parse input into vector
void parse_input(string fname, vector<int> & inp_list, vector<int> & seen_inst) {
    ifstream in(fname);
    string str;
    int counter = 0;
    while (getline(in, str)) {
        if(str.size() > 0) {
            inp_list.push_back(encode(str));
            seen_inst.push_back(0);
            counter++;
        }
    }
    in.close();
}

int run(int & pointer, int & accumulator, vector<int> & inp_list, vector<int> & seen_inst) {
    int inp_size = inp_list.size();
    if (seen_inst[pointer] > 0 || pointer == inp_size) {
        return int(pointer);
    }
    seen_inst[pointer] += 1;
    vector<int> decoded(2);
    decode(inp_list[pointer], decoded); // 1st arg is inst, 2nd arg is value
    int inst = decoded[0], val = decoded[1];

    // run according to inst : 0 for nop, 1 for acc, 2 for jmp
    if (inst == 0) {
        pointer += 1;
    } else if (inst == 1) {
        accumulator += val;
        pointer += 1;
    } else if (inst == 2) {
        pointer += val;
    } else {
        cout << "error: instcode == " << inst << endl; 
    }
    return -1;

}

bool change_inst(vector<int> & inp_copy, int idx) {
    if (abs(inp_copy[idx]) % 10 == 0) {
        inp_copy[idx] += inp_copy[idx] >= 0 ? 2 : -2;
        return true;
    } else if (abs(inp_copy[idx]) % 10 == 2) {
        inp_copy[idx] += inp_copy[idx] >= 0 ? -2 : 2;
        return true;
    }
    return false;
}

int main() {
    string fname = "aoc_day_08_input.txt";
    vector<int> inp_list;
    vector<int> seen_inst;
    int accumulator = 0;
    int pointer = 0;
    parse_input(fname, inp_list, seen_inst); // parse input into a vector
    int inp_size = inp_list.size();
    for (int i = 0; i < inp_list.size(); i++) {
        vector<int> inp_copy(inp_list);
        vector<int> seen_copy(seen_inst);
        pointer = 0;
        accumulator = 0;
        if (change_inst(inp_copy, i)) {
            while(true) {
                int exit_code = run(pointer, accumulator, inp_copy, seen_copy);
                if(exit_code == inp_size) {
                    cout << accumulator << endl;
                    return 0;
                } else if (exit_code > -1) {
                    break;
                }
            }
        }
        
    }
    return 0;
}