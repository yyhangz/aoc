#include "aoc.hpp"
using namespace std;

// parse input into vector
void parse_input(string fname, vector<vector<int>> & group_data) {
    ifstream in(fname);
    string str;
    vector<int> grp_ans(27);
    while (getline(in, str)) {
        if(str.size() > 0) {
            for (auto it = str.cbegin(); it != str.cend(); ++it) {
                grp_ans[char((*it)) - 'a'] += 1;
            }
            grp_ans[26] += 1;
        }
        else {
            group_data.push_back(grp_ans);
            std::fill(grp_ans.begin(), grp_ans.end(), 0);
        }
    }
    group_data.push_back(grp_ans);
    in.close();
}

// check no. of times the ans appears; add only if appears for all members in grp
int check (vector<int> grp_ans) {
    int sum = 0;
    for (int i = 0; i < 26; i++) {
        sum += (grp_ans[i] == grp_ans[26]);
    }
    return sum;
}

int main() {
    string fname = "aoc_day_06_input.txt";
    vector<vector<int>> group_data;
    parse_input(fname, group_data); // parse input into a vector
    int sum = 0;
    // iterate vector to check for no. of ans per grp
    for (auto it = group_data.cbegin(); it != group_data.cend(); ++it) {
         sum += check((*it));
    }
    cout << sum << endl;
    return 0;
}