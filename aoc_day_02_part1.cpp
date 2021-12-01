#include "aoc.hpp"
using namespace std;

// parse input into vector
void parse_input(string fname, vector<vector<string>> & inp_list) {
    ifstream in(fname);
    string str;
    while (getline(in, str)) {
        if(str.size() > 0) {
            stringstream ss(str);
            string word;
            vector<string> *tokens = new vector<string>;
            while (getline(ss, word, ' ')) {
                (*tokens).push_back(word);
            }
            inp_list.push_back(*tokens);
        }
    }
    in.close();
}

// check if password is valid
bool check(int mini, int maxi, char token, string str) {
    int count = 0;
    for (int i = 0; i < str.size(); i++) {
        count += str[i] == token ? 1 : 0;
    }
    return !(count < mini || count > maxi);
}

int main() {
    string fname = "aoc_day_02_input.txt";
    vector<vector<string>> inp_list;
    parse_input(fname, inp_list); // parse input into a vector
    int sum = 0;
    // iterate vector to check for valid passwords
    for (auto i = inp_list.cbegin(); i != inp_list.cend(); ++i) {
        // get mini and maxi
        vector<int> minimax;
        string word;
        stringstream x ((*i)[0]);
        while (getline(x, word, '-')) {
            minimax.push_back(stoi(word));
        }
        sum += check(minimax[0], minimax[1], (*i)[1][0], (*i)[2]) ? 1 : 0;  
    }
    cout << sum << endl;
    return 0;
}