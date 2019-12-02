filename = 'd2_input.txt'

with open(filename, 'r') as f:

    code  = list(map(int,f.read().split(",")))
    code[1], code[2] = int(12), int(2)

    for x in range(int(len(code)/4)):
        if code[4*x] == 99:
            print(f"final code is: {code}")
            break

        elif code[4*x] == 1:
            code[code[4*x+3]] = code[code[4*x+1]] + code[code[4*x+2]]

        elif code[4*x] == 2:
            code[code[4*x+3]] = code[code[4*x+1]] * code[code[4*x+2]]
