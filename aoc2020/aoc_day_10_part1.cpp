#include "aoc.hpp"
using namespace std;

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
    string fname = "aoc_day_10_input.txt";
    vector<int> inp_list;
    int ones = 0, threes = 1, prev = 0;
    parse_input(fname, inp_list);
    sort(inp_list.begin(), inp_list.end());
    for (auto it = inp_list.cbegin(); it != inp_list.cend(); ++it) {
        if (*it - prev == 1) {
            ones++;
        } else {
            threes++;
        }
        prev = (*it);
    }
    cout << ones * threes << endl;
    return 0;
}