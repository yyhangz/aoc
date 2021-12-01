filename = 'd01_input.txt'

adder  = 0

with open(filename, 'r') as f:
    for i in f:
        adder += (int(i)//3) - 2
    print('sum = {0}'.format(adder))
    f.close
