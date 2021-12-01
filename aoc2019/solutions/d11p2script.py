# 0 means to paint the panel black, and 1 means to paint the panel white.
# 0 means it should turn left 90 degrees, and 1 means it should turn right 90 degrees.

filename = 'd11_input'

with open(filename, 'r') as f:
    code = list(map(int,f.read().split(",")))

car_map = {(0 + 0j): 1}
movel = {"U": "L", "L": "D", "D": "R", "R": "U"}
mover = {"U": "R", "R": "D", "D": "L", "L": "U"}
move_by = {"U": 1, "R": 1j, "D": -1, "L": -1j}
curr_dir = "U"
curr_coordi = (0 + 0j)

input_val, x, rbase, op4_do = 0, 0, 0, 0
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
                for i in range(int(addr[y] - len(code) + 1)):
                    code.append(0)

        # Run opcode 1-9
        if opcode == 1:
            code[addr[2]] = int(code[addr[0]] + code[addr[1]])
            x += 4

        elif opcode == 2:
            code[addr[2]] = int(code[addr[0]] * code[addr[1]])
            x += 4
        
        elif opcode == 3:
            if curr_coordi in car_map:
                code[addr[0]] = car_map[curr_coordi]
            else:
                code[addr[0]] = 0
            x += 2

        elif opcode == 4:
            out4 = code[addr[0]]
            # If painting instruction...
            if op4_do == 0:
                car_map[curr_coordi] = out4
                op4_do = 1
            
            # If moving instruction...
            elif op4_do == 1:
                curr_dir = movel[curr_dir] if out4 == 0 else mover[curr_dir]
                curr_coordi += move_by[curr_dir]
                op4_do = 0
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

hull = [[" "] * 42 for i in range(42)]
for item in car_map:
    if car_map[item] == 1:
        hull[int(item.real + 10)][int(item.imag)] = "*"
for x in range(42):
    for item in hull[41 - x]:
        print(item, end="")
    print()
    