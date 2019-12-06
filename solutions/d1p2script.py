def fuelcal(i):
    i = int(i)
    if (i//3 - 2) > 0:
        i = i//3 - 2 + fuelcal(i//3 - 2)
        return i
    else:
        return 0


if __name__ == '__main__':
    filename = 'd1_input.txt'

    adder  = 0

    with open(filename, 'r') as f:
        for i in f:
            adder += fuelcal(int(i))
        print('sum = {0}'.format(adder))
        f.close
