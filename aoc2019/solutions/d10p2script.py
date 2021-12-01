from math import gcd, atan2, pi
import operator

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

ast = (37 + 25j)

vectors = set()
xcoordi = int(ast.real)
ycoordi = int(ast.imag)
for other in astmap:
    if other != ast:
        x = int(other.real)
        y = int(other.imag)
        xvector = int((x - xcoordi))
        yvector = int((y - ycoordi))
        divisor = gcd(xvector, yvector)
        xvector = int(xvector / divisor)
        yvector = int(yvector / divisor)
        vector = (1*xvector + 1j*yvector)
        if vector not in vectors:
            vectors.add(vector)

angle_sort = []
for vector in vectors:
    angle = atan2(-1*vector.imag, vector.real)
    if angle > (pi / 2.0):
        angle -= 2*pi
    angle_sort.append((angle, vector))
angle_sort.sort(key = operator.itemgetter(0), reverse=True)
ans = angle_sort[199][1]

for aster in astmap:
    vec = aster - (37 + 25j)
    if abs(vec/ans) == (vec/ans).real and aster != (37 + 25j):
        print(aster.real*100 + aster.imag)