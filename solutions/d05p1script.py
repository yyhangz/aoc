def output_val(number):
    print(f"output: {number}")

filename = 'd05_input.txt'

with open(filename, 'r') as f:

    code  = list(map(int,f.read().split(",")))

input_val,x = 1, 0
while x < len(code):
    if code[x] == 99:
        print(f"final code is: {code}")
        break
    elif code[x] == 3:
        code[code[x+1]] = input_val
        x += 2
    else:
        instruc = str(code[x]).zfill(4)
        opcode = int(instruc[-2:])
        para = [0, 0]
        assert opcode < 3 or opcode == 4, f"{instruc} {x}"
        if opcode < 3:
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

            elif opcode == 2:
                code[code[x+3]] = int(para[0] * para[1])
            x += 4

        elif opcode == 4:
            if int(instruc[1]) == 0:
                out_val = code[code[x+1]]
            elif int(instruc[1]) == 1:
                out_val = code[x+1]
            output_val(out_val)
            x += 2
        else:
            print(f"Invalid instruction: {instruc}")
