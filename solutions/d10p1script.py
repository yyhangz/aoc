from math import gcd

filename = 'd10_input'
with open(filename, 'r') as f:

    raw = f.read().split('\n')

X = len(raw[0])
Y = len(raw)

astmap = list()
for y in range(Y):
    for x in range(X):
        if raw[y][x] == '#':
            astmap.append((1*x + 1j*y))

ast = 0j
highest = 0

for aster in astmap:
    vectors = set()
    xcoordi = int(aster.real)
    ycoordi = int(aster.imag)
    for other in astmap:
        if other != aster:
            x = int(other.real)
            y = int(other.imag)
            xvector = int((xcoordi - x))
            yvector = int((ycoordi - y))
            divisor = gcd(xvector, yvector)
            xvector = int(xvector / divisor)
            yvector = int(yvector / divisor)
            vector = (1*xvector + 1j*yvector)
            if vector not in vectors:
                vectors.add(vector)
    if len(vectors) > highest:
        highest = len(vectors)
        ast = aster
    
print(highest)
print(ast)