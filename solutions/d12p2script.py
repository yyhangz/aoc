import copy
from math import gcd

moons = [[8, 0, 8], [0, -5, -10], [16, 10, -5], [19, -10, -7]]
velo = [[0, 0, 0] for i in range(4)]

vmap = []
for i in range(3):
    vmap.append([int(moons[0][i]), int(moons[1][i]), int(moons[2][i]), int(moons[3][i]), 0, 0, 0, 0])

vcopy = copy.deepcopy(vmap)

periods = [0, 0, 0]

# Find lowest time period for each coordinate then multiply them tgt
for i in range(3):
    x = 0
    while True:
        # Update velocity
        for k in range(4):
            for l in range(4):
                if vmap[i][k] < vmap[i][l]:
                    vmap[i][k+4] += 1
                
                elif vmap[i][k] > vmap[i][l]:
                    vmap[i][k+4] -= 1
                
                else:
                    continue
            
        # Update coordinate
        for k in range(4):
            vmap[i][k] += vmap[i][k+4]       
        
        x += 1
        # Check if its equal to time period 0
        if vmap[i] == vcopy[i]:
            print(x)
            periods[i] += x
            break

lcm = lambda x,y : int((x * y) / gcd(x, y))

print(lcm(lcm(periods[0], periods[1]), periods[2]))