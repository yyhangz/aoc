from itertools import product

with open("aoc_day_14_input.txt", 'r') as f:
    lines = [line.rstrip() for line in f.read().splitlines()]

def mask(bitmask, val):
    ones_mask = int(bitmask.replace("X", "0"),2)
    zeros_mask = int(bitmask.replace("X", "1"),2)
    val = (int(val) | ones_mask) & zeros_mask
    return val

def replace_address(bitmask, val):
    temp = list(bin(int(val))[2:].zfill(36))
    for i, b in enumerate(bitmask):
        if b != "0":
            temp[i] = b
    return "".join(temp)

def p2_mask(bitmask):
    if not 'X' in bitmask: yield bitmask
    else:
        yield from p2_mask(bitmask.replace('X', '0', 1))
        yield from p2_mask(bitmask.replace('X', '1', 1))

mem = {}
mem2 = {}
bitmask = 0
for line in lines:
    if "mask" in line:
        bitmask = line.split("=")[1][1:]
    else:
        val , key = line.split("=")[1][1:], line.split("=")[0][4:-2]
        mem[key] = mask(bitmask, val)
        new_mask = replace_address(bitmask, key)
        for new_key in p2_mask(new_mask):
            mem2[new_key] = int(val)


print("part 1: " + str(sum([mem[key] for key in mem.keys()])))
print("part 2: " + str(sum([mem2[key] for key in mem2.keys()]))) #4753238784664