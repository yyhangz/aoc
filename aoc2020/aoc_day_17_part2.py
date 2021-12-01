from copy import deepcopy

with open("aoc_day_17_input.txt", 'r') as f:
    start_grid = [list(line.rstrip()) for line in f.readlines()]

class space: 
    def __init__(self, start_grid):
        layers = {0 : deepcopy(start_grid)}
        self.y_len = len(start_grid)
        self.x_len = len(start_grid[0])
        self.hypercube = {0 : deepcopy(layers)}
        self.max_layer, self.min_layer = 0 , 0
        self.max_cube, self.min_cube = 0 , 0

    
    def create_new_layer(self):
        for key in self.hypercube.keys():
            temp = []
            for i in range(self.y_len):
                temp.append([])
                for _ in range(self.x_len):
                    temp[i].append('.')
            self.hypercube[key][self.max_layer + 1] = deepcopy(temp)
            self.hypercube[key][self.min_layer - 1] = deepcopy(temp)
        self.max_layer += 1
        self.min_layer -= 1
    
    def pad_layers(self):
        self.x_len += 2
        self.y_len += 2
        for key in self.hypercube.keys():
            for z in self.hypercube[key]:
                for y in range(len(self.hypercube[key][z])):
                    self.hypercube[key][z][y].insert(0, '.')
                    self.hypercube[key][z][y].append('.')
                null_line = ['.' for _ in range(self.x_len)]
                self.hypercube[key][z].insert(0, deepcopy(null_line))
                self.hypercube[key][z].append(deepcopy(null_line))
    
    def create_new_cube(self):
        null_plane = [['.' for _ in range(self.x_len)] for _ in range(self.y_len)]
        null_cube = {}
        for i in range(self.min_layer, self.max_layer + 1):
            null_cube[i] = deepcopy(null_plane)
        self.hypercube[self.max_cube + 1] = deepcopy(null_cube)
        self.hypercube[self.min_cube - 1] = deepcopy(null_cube)
        self.max_cube += 1
        self.min_cube -= 1
    
    def check_actives(self, x, y, z, w):
        count = 0
        for l in range(-1, 2):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    for k in range(-1, 2):
                        try:
                            if self.hypercube[w + l][z + k][y + j][x + i] == '#' and (l != 0 or k != 0 or j != 0  or i != 0):
                                count += 1
                        except:
                            pass
        return count

    def update_space(self):
        temp_space = deepcopy(self.hypercube)
        for key in self.hypercube.keys():
            for k in range(self.min_layer, self.max_layer + 1):
                for i in range(self.x_len):
                    for j in range(self.y_len):
                        active_count = self.check_actives(i, j, k, key)
                        if self.hypercube[key][k][j][i] == '#':
                            if not(2 <= active_count <= 3):
                                temp_space[key][k][j][i] = '.'
                        elif active_count == 3 and self.hypercube[key][k][j][i] == '.':
                            temp_space[key][k][j][i] = '#'
        self.hypercube = temp_space
    
    def run_cycle(self):
        self.pad_layers()
        self.create_new_layer()
        self.create_new_cube()
        self.update_space()
    
    def count_actives(self):
        count = 0
        for key in self.hypercube.keys():
            for k in range(self.min_layer, self.max_layer + 1):
                for i in range(self.x_len):
                    for j in range(self.y_len):
                        if self.hypercube[key][k][j][i] == '#':
                            count += 1
        return count

myspace = space(start_grid)
for i in range(6):
    myspace.run_cycle()
print(myspace.count_actives())