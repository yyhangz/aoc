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

bool is_correct(string str, unordered_map<char, bool> chars) { // check if chars in umap
    for (int i = 0; i < str.size(); i++) {
        if(chars.find(str[i]) == chars.end()) {
            return false;
        }
    }
    return true;
}

bool valid_entry(string val, string field) { // check if entry is valid based on field
    unordered_map<char, bool> hexa = {{'a', true}, {'b', true}, {'c', true}, {'d', true}, {'e', true},
        {'f', true}, {'0', true}, {'1', true}, {'2', true}, {'3', true}, {'4', true}, {'5', true},
        {'6', true}, {'7', true}, {'8', true}, {'9', true}};
    unordered_map<char, bool> deci = {{'0', true}, {'1', true}, {'2', true}, {'3', true}, {'4', true}, 
        {'5', true}, {'6', true}, {'7', true}, {'8', true}, {'9', true}};
    unordered_map<string, bool> ecol = {{"amb", true}, {"blu", true}, {"brn", true}, {"gry", true}, 
        {"grn", true}, {"hzl", true}, {"oth", true}};
    unordered_map<string, bool> height = {{"cm", true}, {"in", true}};
    if (field == "hcl") {
        return is_correct(val.substr(1), hexa) && val[0] == '#';
    } else if (field == "byr") {
        return is_correct(val, deci) && val.size() == 4 && stoi(val) > 1919 && stoi(val) < 2003;
    } else if (field == "iyr") {
        return is_correct(val, deci) && val.size() == 4 && stoi(val) > 2009 && stoi(val) < 2021;
    } else if (field == "eyr") {
        return is_correct(val, deci) && val.size() == 4 && stoi(val) > 2019 && stoi(val) < 2031;
    } else if (field == "hgt") {
        string unit = val.substr(val.size() - 2);
        if (height.find(unit) == height.end()) {
            return false;
        } else if (unit == "cm") {
            string nums = val.substr(0, 3); 
            return is_correct(nums, deci) && stoi(nums) >= 150 && stoi(nums) <= 193 && val.size() == 5;
        } else if (unit == "in") {
            string nums = val.substr(0, 2); 
            return is_correct(nums, deci) && stoi(nums) >= 59 && stoi(nums) <= 76 && val.size() == 4;
        }
    } else if (field == "ecl") {
        return !(ecol.find(val) == ecol.end());
    } else if (field == "pid") {
        return is_correct(val, deci) && val.size() == 9;
    }
}

// check passport validity
bool check(unordered_map<string, string> person, vector<string> keylist) {
    for (int i = 0; i < keylist.size(); i++) {
        if (person.find(keylist[i]) == person.end()) {
            return false;
        } else if (!(valid_entry(person[keylist[i]], keylist[i]))) {
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