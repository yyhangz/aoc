# Updates the current point on the grid after the instruction, as well as the borders of the grid
def update_grid(instruc, current, xborder, yborder):
    length = int(instruc[1:])
    if instruc[0] == 'R':
        current[0] += length
        if xborder[1] < current[0]: xborder[1] = current[0]
    elif instruc[0] == 'L':
        current[0] -= length
        if xborder[0] > current[0]: xborder[0] = current[0]
    elif instruc[0] == 'U':
        current[1] += length
        if yborder[1] < current[1]: yborder[1] = current[1]
    else:
        current[1] -= length
        if yborder[0] > current[1]: yborder[0] = current[1]


filename = 'd3_input.txt'

with open(filename, 'r') as f:

    cable_one, cable_two = list(f.readline().strip().split(",")), list(f.readline().strip().split(","))


# Initialize current point on grid, and x and y borders of the grid
current, xborder, yborder = [0, 0], [0, 0], [0, 0]
dir = {"L" : 1, "R" : 2, "D" : 3, "U" : 4}

# Create grid
for instruc in cable_one:
    update_grid(instruc, current, xborder, yborder)
grid = [[0] * (yborder[1] - yborder[0] + 1) for i in range(xborder[1] - xborder[0] + 1)]

# Map out cable 1 on grid
new_x, new_y = abs(xborder[0]), abs(yborder[0])
current = [new_x, new_y] # Offset origin to fit grid
for instruc in cable_one:
    length = int(instruc[1:])
    move_dir = dir[instruc[0]]//3 # Account for whether it is moving in x or y axis
    for i in range(length):
        step = ((-1)**dir[instruc[0]])*(i+1) # Determine if you move in positive or negative direction
        x, y = (current[0]) + (abs(move_dir - 1) * step), (current[1]) + (move_dir * step) # Find x and y coordinates on grid
        grid[x][y] = 1
    update_grid(instruc, current, xborder, yborder) # Update current point on grid

current = [abs(xborder[0]), abs(yborder[0])] # Offset origin to fit grid
min_dist = 0
for instruc in cable_two:
    length = int(instruc[1:])
    move_dir = dir[instruc[0]]//3 # Account for whether it is moving in x or y axis
    for i in range(length):
        step = ((-1)**dir[instruc[0]])*(i+1) # Determine if you move in positive or negative direction
        x, y = (current[0]) + (abs(move_dir - 1) * step), (current[1]) + (move_dir * step) # Find x and y coordinates on grid
        try:
            if grid[x][y] == 1:
                cur_dist = abs(x - new_x) + abs(y - new_y)
                if min_dist == 0 or cur_dist<min_dist:
                    min_dist = cur_dist
        except IndexError:
            pass
    update_grid(instruc, current, xborder, yborder) # Update current point on grid

print(min_dist)
