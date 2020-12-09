#include "aoc.hpp"
using namespace std;

void parse_input(string fname, vector<long long> & inp_list, queue<long long> & inp_queue) {
    ifstream in(fname);
    string str;
    while (getline(in, str)) {
        if(str.size() > 0) {
            inp_list.push_back(stoll(str));
            inp_queue.push(stoll(str));
        }
    }
    in.close();
}

void find_minimax(long long & mini, long long & maxi, queue<long long> & contiguous) {
    while (contiguous.size() > 0) {
        mini = mini < contiguous.front() ? mini : contiguous.front();
        maxi = maxi > contiguous.front() ? maxi : contiguous.front();
        contiguous.pop();
    }
}

int main() {
    string fname = "aoc_day_09_input.txt";
    vector<long long> inp_list;
    queue<long long> inp_queue;
    queue<long long> contiguous;
    const long long target = 552655238;
    long long mini = LLONG_MAX, maxi = 0;
    parse_input(fname, inp_list, inp_queue);
    long long sum = 0;
    while(inp_queue.size() > 0) {
        if (sum > target) {
            sum -= contiguous.front();
            contiguous.pop();
        } else if (sum == target) {
            // check min max
            find_minimax(mini, maxi, contiguous);
            cout << mini + maxi << endl;
            return 0;
        } else {
            sum += inp_queue.front();
            contiguous.push(inp_queue.front());
            inp_queue.pop();
        }
    }
    return 0;
}