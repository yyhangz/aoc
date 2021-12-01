import re
import functools

fname = "aoc_day_07_input.txt"
with open(fname) as f:
    lines = f.readlines()

def find_contents(bag):
    if bag == 'no other bag':
        return 0
    else:
        bag_content = [[item[0], item[2:]] for item in bags_info[bag]]
        return functools.reduce(lambda a,b : a + b ,map(lambda x: int(x[0]) + int(x[0]) * find_contents(x[1]), bag_content))

bags_info = {}
for line in lines:
    line = line.replace("bags", "bag").replace("no other", "0 no other")
    x = re.findall(r'\d? ?\w+ \w+ bag', line)
    bags_info[x.pop(0)] = x

print(find_contents('shiny gold bag'))