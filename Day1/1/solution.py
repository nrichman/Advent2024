f = open('input.txt', 'r')

total = 0

for line in f.readlines():
    firstnum = -1
    lastnum = -1
    for c in line:
        if c.isdigit():
            lastnum = c
            if int(firstnum) < 0:
                firstnum = c
    total = total + int(firstnum + lastnum)
print(total)