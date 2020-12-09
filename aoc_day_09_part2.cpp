#include "aoc.hpp"
using namespace std;

void parse_input(string fname, vector<long long> & inp_list) {
    ifstream in(fname);
    string str;
    while (getline(in, str)) {
        if(str.size() > 0) {
            inp_list.push_back(stoll(str));
        }
    }
    in.close();
}

bool run_window(int start, int run_len, long long target, vector<long long> & inp_list) {
    long long sum = 0;
    for (int i = 0; i < run_len; i++) {
        sum += inp_list[start + i];
    }
    return sum == target;
}

void find_minimax(int start, int run_len, long long & mini, long long & maxi, vector<long long> & inp_list) {
    for (int i = 0; i < run_len; i++) {
        mini = mini < inp_list[start + i] ? mini : inp_list[start + i];
        maxi = maxi > inp_list[start + i] ? maxi : inp_list[start + i];
    }
}

int main() {
    string fname = "aoc_day_09_input.txt";
    vector<long long> inp_list;
    const long long target = 552655238;
    long long mini = LLONG_MAX, maxi = 0;
    parse_input(fname, inp_list);
    for (int i = 2; i < inp_list.size(); i++) {
        for (int j = 0; j < inp_list.size() - i; j++) {
            if(run_window(j, i, target, inp_list)) {
                find_minimax(j, i, mini, maxi, inp_list);
                cout << mini + maxi << endl;
                return 0;
            }
        }
    }
    return 0;
}