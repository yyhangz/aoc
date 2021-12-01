import re
import functools

fname = "aoc_day_07_input.txt"
with open(fname) as f:
    lines = f.readlines()

def find_shiny(bag):
    if bag == 'shiny gold bag':
        return True
    elif bag == 'no other bag':
        return False
    else:
        return functools.reduce(lambda a,b : a or b ,map(lambda x: find_shiny(x), bags_info[bag]))

bags_info = {}
for line in lines:
    line = line.replace("bags", "bag")
    x = re.findall(r'\w+ \w+ bag', line)
    bags_info[x.pop(0)] = x

bags_list = list(bags_info.keys())
bags_list.remove('shiny gold bag')
print(list(map(find_shiny, bags_list)).count(True))