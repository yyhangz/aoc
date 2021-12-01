#include "aoc.hpp"
using namespace std;

// parse input into vector
void parse_input(string fname, unordered_map<int,vector<int>> & inp_map, int & prev) {
    ifstream in(fname);
    string str;
    int count = 1;
    while (getline(in, str)) {
        if(str.size() > 0) {
            stringstream ss(str);
            string token;
            while (getline(ss, token, ',')) {
                vector<int> temp = {count};
                inp_map.insert({stoi(token),temp});
                prev = stoi(token);
                count++;
            }
        }
    }
    in.close();
}

int main() {
    string fname = "aoc_day_15_input.txt";
    long mem[2] = {2020, 30000000};
    for (int i = 0; i < 2; i++) {
        unordered_map<int, vector<int>> inp_map;
        int prev;
        parse_input(fname, inp_map, prev); // parse input into a vector
        for (int turns = inp_map.size() + 1; turns < mem[i] + 1; turns++) {
            int curr;
            if (inp_map[prev].size() == 1) {
                curr = 0;
            } else {
                curr = inp_map[prev][inp_map[prev].size() - 1] - inp_map[prev][inp_map[prev].size() - 2];
            }
            if (inp_map.find(curr) == inp_map.end()) {
                vector<int> temp = {turns};
                inp_map.insert({curr, temp});
            } else {
                inp_map[curr].push_back(turns);
            }
            prev = curr;
        }
        cout << "part " << i + 1 << ": " << prev << endl;
    }
    return 0;
}