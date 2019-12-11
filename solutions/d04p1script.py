minval, maxval = 156218, 652527
current  = minval

count = 0

while current < maxval:
    cur_str = str(current)
    adj = False
    ascend = True
    for i in range(5):
        if int(cur_str[i]) < int(cur_str[i+1]):
            pass
        elif int(cur_str[i]) == int(cur_str[i+1]):
            adj = True
        else:
            ascend = False
            break
    if adj and ascend:
        count += 1
    current += 1
print(count)
