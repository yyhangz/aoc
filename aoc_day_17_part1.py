from copy import deepcopy

with open("aoc_day_17_input.txt", 'r') as f:
    start_grid = [list(line.rstrip()) for line in f.readlines()]

class space: 
    def __init__(self, start_grid):
        self.y_len = len(start_grid)
        self.x_len = len(start_grid[0])
        self.layers = {0 : deepcopy(start_grid)}
        self.max_layer = 0
        self.min_layer = 0
    
    def create_new_layer(self):
        temp = []
        for i in range(self.y_len):
            temp.append([])
            for _ in range(self.x_len):
                temp[i].append('.')
        self.layers[self.max_layer + 1] = deepcopy(temp)
        self.layers[self.min_layer - 1] = deepcopy(temp)
        self.max_layer += 1
        self.min_layer -= 1
    
    def pad_layers(self):
        self.x_len += 2
        self.y_len += 2
        for key in self.layers.keys():
            for y in range(len(self.layers[key])):
                self.layers[key][y].insert(0, '.')
                self.layers[key][y].append('.')
            null_line = ['.' for _ in range(self.x_len)]
            self.layers[key].insert(0, deepcopy(null_line))
            self.layers[key].append(deepcopy(null_line))
    
    def check_actives(self, x, y, z):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    try:
                        if self.layers[z + k][y + j][x + i] == '#' and (k != 0 or j != 0  or i != 0):
                            count += 1
                    except:
                        pass
        return count

    def update_space(self):
        temp_space = deepcopy(self.layers)
        for key in self.layers.keys():
            for i in range(self.x_len):
                for j in range(self.y_len):
                    active_count = self.check_actives(i, j, key)
                    if self.layers[key][j][i] == '#':
                        if not(2 <= active_count <= 3):
                            temp_space[key][j][i] = '.'
                    elif active_count == 3 and self.layers[key][j][i] == '.':
                        temp_space[key][j][i] = '#'
        self.layers = temp_space
    
    def run_cycle(self):
        self.pad_layers()
        self.create_new_layer()
        self.update_space()
    
    def count_actives(self):
        count = 0
        for key in self.layers.keys():
            for i in range(self.x_len):
                for j in range(self.y_len):
                    if self.layers[key][j][i] == '#':
                        count += 1
        return count

myspace = space(start_grid)
for i in range(6):
    myspace.run_cycle()
print(myspace.count_actives())