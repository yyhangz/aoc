#include "aoc.hpp"
using namespace std;

// parse input into vector
void parse_input(string fname, vector<string> & inp_list) {
    ifstream in(fname);
    string str;
    while (getline(in, str)) {
        if(str.size() > 0) {
            inp_list.push_back(str);
        }
    }
    in.close();
}

int convert_bin(string str) {
    int sum = 0;
    for (int i = 0; i < str.size(); i++) {
        sum <<= 1;
        sum |= (str[i] == 'B' || str[i] == 'R');
    }
    return sum;
}

int calc_seat(int row, int col) {
    return row * 8 + col;
}

// find seat whose +1 and -1 are occupied
int find_seat(vector<int> seats) {
    int prev = -1;
    for (int i = 0; i < seats.size(); i++) {
        if (seats[i] - 2 == prev) {
            return seats[i] - 1;
        }
        prev = seats[i];
    }
}

int main() {
    string fname = "aoc_day_05_input.txt";
    vector<string> inp_list;
    parse_input(fname, inp_list); // parse input into a vector
    vector<int> seats;
    
    // calc seat number for each line of input
    for (auto i = inp_list.cbegin(); i != inp_list.cend(); ++i) {
        int curr = calc_seat(convert_bin((*i).substr(0, 7)), convert_bin((*i).substr(7)));
        seats.push_back(curr);
    }

    sort(seats.begin(), seats.end()); 
    cout << find_seat(seats) << endl;
}