#include "aoc.hpp"
using namespace std;

// parse input into vector
void parse_input(string fname, vector<int> & inp_list) {
    ifstream in(fname);
    string str;
    while (getline(in, str)) {
        if(str.size() > 0) {
            inp_list.push_back(stoi(str));
        }
    }
    in.close();
}

int main() {
    string fname = "aoc_day_01_input.txt";
    vector<int> inp_list;
    unordered_map<int, int> inp_map;
    parse_input(fname, inp_list); // parse input into a vector
    
    // makes unordered map with the values as keys
    for (auto i = inp_list.cbegin(); i != inp_list.cend(); ++i) {
        // cout << *i << endl;
        inp_map[*i] = true;
    }

    // check for the 2 entries that add to 2020
    for (auto i = inp_list.cbegin(); i != inp_list.cend(); ++i) {
        if(inp_map[*i] && inp_map[2020 - *i]) {
            cout << *i * (2020 - *i) << endl;
            return 0;
        }
    }
}