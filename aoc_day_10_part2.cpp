#include "aoc.hpp"
using namespace std;

void parse_input(string fname, vector<int> & inp_list) {
    ifstream in(fname);
    string str;
    inp_list.push_back(0);
    while (getline(in, str)) {
        if(str.size() > 0) {
            inp_list.push_back(stoi(str));
        }
    }
    in.close();
}

int check_prev(int i, vector<int> & inp_list){
    int count = 0;
    if (i-1 >= 0 && inp_list[i]-inp_list[i-1] <= 3)
        count++;
    if (i-2 >= 0 && inp_list[i]-inp_list[i-2] <= 3)
        count++;
    if (i-3 >= 0 && inp_list[i]-inp_list[i-3] <= 3)
        count++;
    return count;
}

int main() {
    string fname = "aoc_day_10_input.txt";
    vector<int> inp_list;
    parse_input(fname, inp_list);
    sort(inp_list.begin(), inp_list.end());
    vector<long long> db(inp_list.size());
    db[0] = 1;
    for (int i = 1; i < inp_list.size(); i++) {
        int num_prev = check_prev(i, inp_list);
        if(num_prev == 1)
            db[i] = db[i-1];
        else if (num_prev == 2)
            db[i] = db[i-1] + db[i-2];
        else if (num_prev == 3)
            db[i] = db[i-1] + db[i-2] + db[i-3];
    }
    cout << db[inp_list.size() - 1] << endl;
    return 0;
}