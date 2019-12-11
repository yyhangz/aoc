filename = 'd09_input'

with open(filename, 'r') as f:
    code = list(map(int,f.read().split(",")))

input_val, x, rbase = 2, 0, 0
while True:
    # Exit intcode if opcode is 99
    if code[x] == 99:
        break
    else:
        # Make instruction 5 digits
        instruc = str(code[x]).zfill(5)
        opcode = int(instruc[-2:])
        
        # Calculate addresses of the 3 parameters
        addr = [0, 0, 0]
        assert opcode < 10, f"{instruc} {x}"
        for y in range(3):
            if int(instruc[2-y]) == 0:
                addr[y] = code[x+y+1]
            elif int(instruc[2-y]) == 1:
                addr[y] = x+y+1
            elif int(instruc[2-y]) == 2:
                addr[y] = code[x+y+1] + rbase
            else:
                print(f"Invalid parameter code: {instruc}")
                exit()

            # Expand memory size if needed
            if addr[y] > len(code):
                for i in range(int(addr[y] - len(code))):
                    code.append(0)

        # Run opcode 1-9
        if opcode == 1:
            code[addr[2]] = int(code[addr[0]] + code[addr[1]])
            x += 4

        elif opcode == 2:
            code[addr[2]] = int(code[addr[0]] * code[addr[1]])
            x += 4
        
        elif opcode == 3:
            code[addr[0]] = input_val
            x += 2

        elif opcode == 4:
            print(code[addr[0]])
            x += 2

        elif opcode == 5:
            if code[addr[0]] != 0:
                x = code[addr[1]]
            else:
                x += 3

        elif opcode == 6:
            if code[addr[0]] == 0:
                x = code[addr[1]]
            else:
                x += 3

        elif opcode == 7:
            if code[addr[0]] < code[addr[1]]:
                code[addr[2]] = 1
            else:
                code[addr[2]] = 0
            x += 4

        elif opcode == 8:
            if code[addr[0]] == code[addr[1]]:
                code[addr[2]] = 1
            else:
                code[addr[2]] = 0
            x += 4
        elif opcode == 9:
            rbase += code[addr[0]]
            x += 2
        else:
            print(f"Invalid instruction: {instruc}")