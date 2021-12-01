#include "aoc.hpp"
using namespace std;

// parse input into vector
void parse_input(string fname, vector<set<int>> & group_data) {
    ifstream in(fname);
    string str;
    set<int> grp_ans;
    while (getline(in, str)) {
        if(str.size() > 0) {
            for (auto it = str.cbegin(); it != str.cend(); ++it) {
                grp_ans.insert((*it));
            }
        }
        else {
            group_data.push_back(grp_ans);
            grp_ans.clear();
        }
    }
    group_data.push_back(grp_ans);
    in.close();
}

int main() {
    string fname = "aoc_day_06_input.txt";
    vector<set<int>> group_data;
    parse_input(fname, group_data); // parse input into a vector
    int sum = 0;
    // iterate vector to check for no. of ans per grp
    for (auto it = group_data.cbegin(); it != group_data.cend(); ++it) {
         sum += (*it).size();
    }
    cout << sum << endl;
    return 0;
}