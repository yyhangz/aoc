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
    unsigned long width = inp_list[0].size(), fproduct = 1; // no. of tiles in each row
    vector<vector<int>> slopes = {{1,1}, {3,1}, {5,1}, {7,1}, {1,2}};
    // check for trees for all entries of slopes
    for (auto i = slopes.cbegin(); i != slopes.cend(); ++i) {
        int sum = 0, curr = 0;
        for (int j = 0; j < inp_list.size(); j+= (*i)[1]) {
            sum += check(curr, inp_list[j]);
            curr = (curr + (*i)[0]) % width;
        }
        fproduct *= sum;
    }
    cout << fproduct << endl;
    return 0;
}