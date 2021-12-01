filename = 'd02_input.txt'

with open(filename, 'r') as f:

    og_code  = list(map(int,f.read().split(",")))

    target = 19690720

    code = []
    for i in range(100*100):
        code = list(og_code)
        code[1], code[2] = i%100, i//100
        for x in range(int(len(code)/4)):
            if code[4*x] == 99:
                if code[0] == target:
                    print(100*code[1]+code[2])
                    exit()
                else:
                    break

            elif code[4*x] == 1:
                try:
                    code[code[4*x+3]] = code[code[4*x+1]] + code[code[4*x+2]]
                except:
                    break

            elif code[4*x] == 2:
                try:
                    code[code[4*x+3]] = code[code[4*x+1]] * code[code[4*x+2]]
                except:
                    break
