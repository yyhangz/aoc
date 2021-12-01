#include "aoc.hpp"
using namespace std;

// parse input into vector
void parse_input(string fname, vector<vector<char>> & inp_list) {
    ifstream in(fname);
    string str;
    while (getline(in, str)) {
        if(str.size() > 0) {
            vector<char> tokens;
            for (int i = 0; i < str.size(); i++) {
                tokens.push_back(str[i]);
            }
            inp_list.push_back(tokens);
        }
    }
    in.close();
}

// check if theres a tree on current tile
bool check(int curr, vector<char> row) {
    return row[curr] == char('#');
}

int main() {
    string fname = "aoc_day_03_input.txt";
    vector<vector<char>> inp_list;
    parse_input(fname, inp_list); // parse input into a vector
    int width = inp_list[0].size(), curr = 0, sum = 0; // width == no. of tiles in each row
    // iterate vector, moving 3 right and 1 down to check for trees
    for (auto i = inp_list.cbegin(); i != inp_list.cend(); ++i) {
        sum += check(curr, *i);
        curr = (curr + 3) % width;
    }
    cout << sum << endl;
    return 0;
}