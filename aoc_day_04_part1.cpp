#include "aoc.hpp"
using namespace std;

// parse input into vector
void parse_input(string fname, vector<unordered_map<string, string>> & persons_data) {
    ifstream in(fname);
    string str;
    unordered_map<string, string> person_info;
    while (getline(in, str)) {
        if(str.size() > 0) {
            stringstream ss(str);
            string word;
            while (getline(ss, word, ' ')) {
                stringstream keypair(word);
                vector<string> val;
                string temp;
                while (getline(keypair, temp, ':')) {
                    val.push_back(temp);
                }
                person_info[val[0]] = val[1];
            }
        }
        else {
            persons_data.push_back(person_info);
            person_info.clear();
        }
    }
    persons_data.push_back(person_info);
    in.close();
}

// check passport
bool check(unordered_map<string, string> person, vector<string> keylist) {
    for (int i = 0; i < keylist.size(); i++) {
        if (person.find(keylist[i]) == person.end()) {
            return false;
        }
    }
    return true;
}

int main() {
    string fname = "aoc_day_04_input.txt";
    vector<unordered_map<string, string>> persons_data;
    parse_input(fname, persons_data); // parse input into a vector
    int sum = 0;
    vector<string> keylist = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};
    // iterate vector to check for valid passports
    for (int i = 0; i < persons_data.size(); i++) {
        sum += check(persons_data[i], keylist);  
    }
    cout << sum << endl;
    return 0;
}