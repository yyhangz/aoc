from itertools import permutations 

filename = 'd7_input'

with open(filename, 'r') as f:

    code = list(map(int,f.read().split(",")))


def intcode(phase, amp):
    global outval
    global running
    code = code_copy[amp]
    while ikeys[amp] < len(code):
        if code[ikeys[amp]] == 99:
            if amp == 4:
                running = False
            break
        
        elif code[ikeys[amp]] == 3:
            if pkeys[amp]:
                code[code[ikeys[amp]+1]] = phase
                pkeys[amp] = False
            else:
                code[code[ikeys[amp]+1]] = outval
            ikeys[amp] += 2

        else:
            instruc = str(code[ikeys[amp]]).zfill(4)
            opcode = int(instruc[-2:])
            para = [0, 0]
            assert opcode < 9 and opcode != 3
            if opcode != 4:
                for y in range(2):
                    if int(instruc[1-y]) == 0:
                        para[y] = code[code[ikeys[amp]+y+1]]
                    elif int(instruc[1-y]) == 1:
                        para[y] = code[ikeys[amp]+y+1]

                if opcode == 1:
                    code[code[ikeys[amp]+3]] = int(para[0] + para[1])
                    ikeys[amp] += 4

                elif opcode == 2:
                    code[code[ikeys[amp]+3]] = int(para[0] * para[1])
                    ikeys[amp] += 4

                elif opcode == 5:
                    if para[0] != 0:
                        ikeys[amp] = para[1]
                    else:
                        ikeys[amp] += 3

                elif opcode == 6:
                    if para[0] == 0:
                        ikeys[amp] = para[1]
                    else:
                        ikeys[amp] += 3

                elif opcode == 7:
                    if para[0] < para[1]:
                        code[code[ikeys[amp]+3]] = 1
                    else:
                        code[code[ikeys[amp]+3]] = 0
                    ikeys[amp] += 4

                elif opcode == 8:
                    if para[0] == para[1]:
                        code[code[ikeys[amp]+3]] = 1
                    else:
                        code[code[ikeys[amp]+3]] = 0
                    ikeys[amp] += 4

            elif opcode == 4:
                outval = int(code[code[ikeys[amp]+1]])
                ikeys[amp] += 2
                return
            else:
                print(f"Invalid instruction: {instruc}")



phase_combi = list(permutations(range(5, 10)))
outval = 0
running = True
thrust_val = []

for phase in phase_combi:
    ikeys = {}
    for i in range(5): ikeys[i] = 0
    pkeys = {}
    for i in range(5): pkeys[i] = True
    code_A = code.copy()
    code_B = code.copy()
    code_C = code.copy()
    code_D = code.copy()
    code_E = code.copy()
    code_copy = [code_A, code_B, code_C, code_D, code_E]
    outval = 0
    while running:
        for amp in range(5):
            intcode(phase[amp], amp)
    thrust_val.append(outval)
    running = True

print(max(thrust_val))