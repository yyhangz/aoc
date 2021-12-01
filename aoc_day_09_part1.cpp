#include "aoc.hpp"
using namespace std;

void parse_input(string fname, set<long long> & inp_set, queue<long long> & curr25, queue<long long> & remaining) {
    ifstream in(fname);
    string str;
    int counter = 0;
    while (getline(in, str)) {
        if(str.size() > 0) {
            if (counter < 25) {
                inp_set.insert(stoll(str));
                curr25.push(stoll(str));
                counter++;
            } else {
                remaining.push(stoll(str));
            }
        }
    }
    in.close();
}

int main() {
    string fname = "aoc_day_09_input.txt";
    set<long long> inp_set;
    queue<long long> curr25, remaining;
    parse_input(fname, inp_set, curr25, remaining);
    while(remaining.size() > 0) {
        long long current = remaining.front();
        bool valid = false;
        for (const long long &number : inp_set) {
            if (inp_set.find(current - number) != inp_set.end()) {
                valid = true;
                break;
            }
        }
        if (!valid) {
            cout << current << endl;
            return 0;
        }
        remaining.pop();
        curr25.push(current);
        inp_set.insert(current);
        inp_set.erase(curr25.front());
        curr25.pop();
    }
    return 0;
}