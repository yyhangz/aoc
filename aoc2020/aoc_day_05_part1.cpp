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

int main() {
    string fname = "aoc_day_05_input.txt";
    vector<string> inp_list;
    parse_input(fname, inp_list); // parse input into a vector
    int maxi = 0;
    
    // calc seat number for each line of input and get max
    for (auto i = inp_list.cbegin(); i != inp_list.cend(); ++i) {
        int curr = calc_seat(convert_bin((*i).substr(0, 7)), convert_bin((*i).substr(7)));
        maxi = maxi < curr ? curr : maxi;
    }
    cout << maxi << endl;
}