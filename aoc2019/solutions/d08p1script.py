filename = 'd08_input'

with open(filename, 'r') as f:

    n = 25*6
    raw = f.read().strip()
    layers = [raw[i:i+n] for i in range(0, len(raw), n)]

least_zeros = 25*6 + 1
layer_id = 100
for x in range(len(layers)):
    y = layers[x].count('0')
    if y < least_zeros:
        least_zeros, layer_id = y, x

chosen = str(layers[layer_id])
print(chosen.count('1') * chosen.count('2'))