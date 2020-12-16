with open("aoc_day_16_input.txt", 'r') as f:
    data = [line.strip() for line in f.read().splitlines() if (line != '' and "your" not in line and "nearby" not in line)]
vrange = []
errors = []
invalids = []
valids = {}
for line_num, line in enumerate(data):
    if ':' in line:
        vrange.append([int(num) for x in line.split(':')[1][1:].split(" or ") for num in x.split("-")])
        valids[line_num] = [i for i in range(20)]
    else:
        is_valid_line = True
        for num in line.split(','):
            is_valid = False
            for ranges in vrange:
                if ranges[0] <= int(num) <= ranges[1] or ranges[2] <= int(num) <= ranges[3]:
                    is_valid = True
                    break
            if not is_valid: 
                errors.append(int(num))
                is_valid_line = False
        if is_valid_line:
            for i, num in enumerate(line.split(',')):
                for j, ranges in enumerate(vrange):
                    if ranges[0] <= int(num) <= ranges[1] or ranges[2] <= int(num) <= ranges[3]:
                        pass
                    else:
                        valids[j].remove(i)

print(f'part 1: {sum(errors)}')

final = {}
result = 1
for key in sorted(valids, key=lambda i: len(valids[i])):
    for index in valids[key]:
            if index not in final.values():
                final[key] = index
                if "depart" in data[key]:
                    result *= int(data[20].split(',')[index])

print(f'part 2: {result}')