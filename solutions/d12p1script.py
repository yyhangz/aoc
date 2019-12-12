moons = [[8, 0, 8], [0, -5, -10], [16, 10, -5], [19, -10, -7]]
velo = [[0, 0, 0] for i in range(4)]

for x in range(1000):
    for moon in moons:
        y = moons.index(moon)
        for others in moons:
            for i in range(3):
                if moon[i] < others[i]:
                    velo[y][i] += 1
                elif moon[i] > others[i]:
                    velo[y][i] -= 1
                else:
                    continue
    for moon in moons:
        y = moons.index(moon)
        for i in range(3):
            moon[i] += velo[y][i]
    
sum = 0
for y in range(4):
    kin = 0
    pot = 0
    for z in range(3):
        pot += abs(moons[y][z])
        kin += abs(velo[y][z])
    sum += (kin*pot)

print(sum)