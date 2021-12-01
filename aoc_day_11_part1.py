import copy 

with open("aoc_day_11_input.txt", 'r') as f:
    data = [[letter for letter in line.strip()] for line in f.readlines()]
prev = 0
curr = copy.deepcopy(data)

def update():
    for i in range(len(prev)):
        for j in range(len(prev[0])):
            occupied = num_occ(i, j)
            if occupied == 0 and prev[i][j] == 'L':
                curr[i][j] = '#'
            elif occupied >= 4 and prev[i][j] == '#':
                curr[i][j] = 'L'

def num_occ(row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                count += 1 if is_occupied(row+i, col+j) else 0
    return count

def is_occupied(row, col):
    if 0 <= row < len(prev) and 0 <= col < len(prev[0]):
        return prev[row][col] == '#'
    return False


while(prev != curr):
    prev = copy.deepcopy(curr)
    update()

print(sum([line.count('#') for line in curr]))