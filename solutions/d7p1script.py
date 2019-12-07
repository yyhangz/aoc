from itertools import permutations 

filename = 'd7_input'

with open(filename, 'r') as f:

    code = list(map(int,f.read().split(",")))


def intcode(input_one, input_two, code):
    x = 0
    choose_input = True
    while x < len(code):
        if code[x] == 99:
            break
        elif code[x] == 3:
            if choose_input:
                code[code[x+1]] = input_one
                choose_input = False
            else:
                code[code[x+1]] = input_two
            x += 2
        else:
            instruc = str(code[x]).zfill(4)
            opcode = int(instruc[-2:])
            para = [0, 0]
            assert opcode < 9 and opcode != 3, f"{instruc} {x}"
            if opcode != 4:
                for y in range(2):
                    if int(instruc[1-y]) == 0:
                        para[y] = code[code[x+y+1]]
                    elif int(instruc[1-y]) == 1:
                        para[y] = code[x+y+1]
                    else:
                        print(f"Invalid parameter code: {instruc}")
                        exit()

                if opcode == 1:
                    code[code[x+3]] = int(para[0] + para[1])
                    x += 4

                elif opcode == 2:
                    code[code[x+3]] = int(para[0] * para[1])
                    x += 4

                elif opcode == 5:
                    if para[0] != 0:
                        x = para[1]
                    else:
                        x += 3

                elif opcode == 6:
                    if para[0] == 0:
                        x = para[1]
                    else:
                        x += 3

                elif opcode == 7:
                    if para[0] < para[1]:
                        code[code[x+3]] = 1
                    else:
                        code[code[x+3]] = 0
                    x += 4

                elif opcode == 8:
                    if para[0] == para[1]:
                        code[code[x+3]] = 1
                    else:
                        code[code[x+3]] = 0
                    x += 4

            elif opcode == 4:
                if int(instruc[1]) == 0:
                    return int(code[code[x+1]])
                elif int(instruc[1]) == 1:
                    return int(code[x+1])
                x += 2
            else:
                print(f"Invalid instruction: {instruc}")


phase_combi = list(permutations(range(0, 5))) 
outval = 0
thrust_val = []
code_copy = list(code)
for phase in phase_combi:
    outval = 0
    for setting in phase:
        outval = intcode(int(setting), outval, code_copy)
        code_copy = list(code)
    thrust_val.append(outval)

print(max(thrust_val))