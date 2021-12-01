#include "aoc.hpp"
using namespace std;

// parse input into vector
void parse_input(string fname, vector<pair<char, int>> & inp_list) {
    ifstream in(fname);
    string str;
    while (getline(in, str)) {
        if(str.size() > 0) {
            pair<char, int> instr;
            instr.first = str[0];
            instr.second = stoi(str.substr(1));
            inp_list.push_back(instr);
        }
    }
    in.close();
}

int norm_angle(int x) {
    x = fmod(x + 180,360);
    if (x < 0)
        x += 360;
    return x - 180;
}

void run_instr(char instr, int val, int & longi, int & lati, int & angle) {
    if (instr == 'N')
        lati += val;
    else if (instr == 'S')
        lati -= val;
    else if (instr == 'E')
        longi += val;
    else if (instr == 'W')
        longi -= val;
    else if (instr == 'R')
        angle = norm_angle(angle - val);
    else if (instr == 'L')
        angle = norm_angle(angle + val);
    else {
        if (angle == 90 || angle == -90)
            lati += (angle/abs(angle)) * val;
        else
            longi += angle == 0 ? val : -1 * val;
    }
}

void run_instr_2(char instr, int val, int & longi, int & lati, pair<int, int> & waypoint) {
    if (instr == 'N')
        waypoint.second += val;
    else if (instr == 'S')
        waypoint.second -= val;
    else if (instr == 'E')
        waypoint.first += val;
    else if (instr == 'W')
        waypoint.first -= val;
    else if (instr == 'R') {
        int angle = norm_angle(-1 * val);
        int first_tmp = waypoint.first;
        waypoint.first = (angle % -180 == 0) 
            ? (angle == 0) ? waypoint.first : -1 * waypoint.first
            : (abs(angle)/angle == 1) ? -1 * waypoint.second : waypoint.second;
        waypoint.second = (angle % -180 == 0) 
            ? (angle == 0) ? waypoint.second : -1 * waypoint.second
            : (abs(angle)/angle == 1) ? first_tmp : -1 * first_tmp;   
    } else if (instr == 'L') {
        int angle = norm_angle(val);
        int first_tmp = waypoint.first;
        waypoint.first = (angle % -180 == 0) 
            ? (angle == 0) ? waypoint.first : -1 * waypoint.first
            : (abs(angle)/angle == 1) ? -1 * waypoint.second : waypoint.second;
        waypoint.second = (angle % -180 == 0) 
            ? (angle == 0) ? waypoint.second : -1 * waypoint.second
            : (abs(angle)/angle == 1) ? first_tmp : -1 * first_tmp;  
    } else {
        lati += waypoint.second * val;
        longi += waypoint.first * val;
    }
}

int main() {
    string fname = "aoc_day_12_input.txt";
    vector<pair<char, int>> inp_list;
    parse_input(fname, inp_list); // parse input into a vector
    int longi = 0, lati = 0, angle = 0;
    pair<int, int> waypoint(10, 1);
    // part 1
    for (auto i = inp_list.cbegin(); i != inp_list.cend(); ++i) {
        run_instr((*i).first, (*i).second, longi, lati, angle);
    }
    cout << "part 1: " << abs(longi) + abs(lati) << endl;
    // part 2
    longi = 0, lati = 0;
    for (auto i = inp_list.cbegin(); i != inp_list.cend(); ++i) {
        run_instr_2((*i).first, (*i).second, longi, lati, waypoint);
    }
    cout << "part 2: "<< abs(longi) + abs(lati) << endl;
}