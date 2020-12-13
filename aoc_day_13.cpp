#include "aoc.hpp"
using namespace std;

// parse input into vector
void parse_input(string fname, vector<string> & inp_list) {
    ifstream in(fname);
    string str;
    while (getline(in, str)) {
        if(str.size() > 0) {
            stringstream ss(str);
            string token;
            while(getline(ss, token, ',')) {
                inp_list.push_back(token);
            }
        }
    }
    in.close();
}

int main() {
    string fname = "aoc_day_13_input.txt";
    vector<string> inp_list;
    parse_input(fname, inp_list); // parse input into a vector
    int time = stoi(inp_list[0]);
    pair<int, int> earliest(0, INT_MAX);
    // part 1
    for (int i = 1; i < inp_list.size(); i++) {
        if (inp_list[i] != "x") {  
            int bus_id = stoi(inp_list[i]);
            int bus_time = bus_id - (time % bus_id);
            if (bus_time < earliest.second) {
                earliest.first = bus_id;
                earliest.second = bus_time;
            }
        }
    }
    cout << "part 1: " << earliest.first * earliest.second << endl;
    
    // part 2
    vector<pair<int, int>> bus_steps; // 1st arg is bus id, 2nd is mins aft timestamp
    for (int i = 1; i < inp_list.size(); i++) {
        if (inp_list[i] != "x") {
            int id = stoi(inp_list[i]);
            bus_steps.push_back(make_pair(id - (i-1) % id, id));
        }
    }
    long long t = 0;
    long long multiplier = bus_steps[0].second;
    for (int i = 1; i < bus_steps.size(); i++) {
        while ( ( t % bus_steps[i].second ) != bus_steps[i].first ) {
            t += multiplier;
        }
        multiplier *= bus_steps[i].second;
    }
    cout << "part 2: " << t << endl;

}