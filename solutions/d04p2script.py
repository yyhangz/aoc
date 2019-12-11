minval, maxval = 156218, 652527
current  = minval

count = 0

while current < maxval:
    cur_str = str(current)
    combo = 0
    adj = False
    ascend = True
    for i in range(5):
        if int(cur_str[i]) < int(cur_str[i+1]):
            if combo == 1:
                adj = True
            combo = 0
        elif int(cur_str[i]) == int(cur_str[i+1]):
            combo += 1
        else:
            ascend = False
            break
    if (adj or combo == 1) and ascend:
        count += 1
    current += 1
print(count)
