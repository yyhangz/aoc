''' Every three output instructions specify the x position (distance from the left), y position (distance from the top), and tile id.
    The tile id is interpreted as follows:
    0 is an empty tile. No game object appears in this tile.
    1 is a wall tile. Walls are indestructible barriers.
    2 is a block tile. Blocks can be broken by the ball.
    3 is a horizontal paddle tile. The paddle is indestructible.
    4 is a ball tile. The ball moves diagonally and bounces off objects.
'''

filename = 'd13_input'

with open(filename, 'r') as f:
    code = list(map(int,f.read().split(",")))

board = {}
coordi = (0 + 0j)
blocks = 0

inval, x, rbase, op4_do = 0, 0, 0, 0
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
                for i in range(int(addr[y] - len(code) + 2)):
                    code.append(0)

        # Run opcode 1-9
        if opcode == 1:
            code[addr[2]] = int(code[addr[0]] + code[addr[1]])
            x += 4

        elif opcode == 2:
            code[addr[2]] = int(code[addr[0]] * code[addr[1]])
            x += 4
        
        elif opcode == 3:
            # code[addr[0]] = inval (Not needed for p1)
            x += 2

        elif opcode == 4:
            out4 = code[addr[0]]            
            # If xcoordi instruction
            if op4_do == 0:
                coordi = out4
                op4_do = 1
            
            # If ycoordi instruction
            elif op4_do == 1:
                coordi += (1j * out4)
                op4_do = 2
            
            # If tile instruction
            elif op4_do == 2:
                board[coordi] = out4
                if out4 == 2:
                    blocks += 1
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

print(blocks)