filename = 'd8_input'

with open(filename, 'r') as f:

    n = 25*6
    raw = f.read().strip()
    layers = [raw[i:i+n] for i in range(0, len(raw), n)]

pic = ['2' for i in range(25*6)]
for x in range(len(layers)):
    for digit in range(25*6):
        if pic[digit] == '2':
            pic[digit] = layers[x][digit]

final = ''.join(pic)
final = final.replace("0", " ").replace("1", ".")
for i in range(0, 25*6, 25):
    print(final[i:i+25])