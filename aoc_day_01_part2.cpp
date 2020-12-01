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

// finds the 2 terms that reach target (the 2 terms cannot include first_term) 
int find_sum(int target, int first_term, vector<int> & inp_list, unordered_map<int, int> & inp_map) {
    for (auto i = inp_list.cbegin(); i != inp_list.cend(); ++i) {
        if(inp_map[*i] && inp_map[target - *i]) {
            if (!(*i == first_term || target - *i ==  first_term)) {
                cout << *i * (target - *i) * first_term << endl;
                return 1;
            }
        }
    }
    return 0;
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

    // check for the 3 entries that add to 2020
    for (auto i = inp_list.cbegin(); i != inp_list.cend(); ++i) {
        if(find_sum(2020 - *i, *i, inp_list, inp_map)) {
            return 0;
        }
    }
    return 0;
}