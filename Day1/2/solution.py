f = open('input.txt', 'r')

total = 0

nums3 = {
    'one': '1',
    'two': '2',
    'six': '6',
}

nums4 = {
    'four': '4',
    'five': '5',
    'nine': '9',
}

nums5 = {
    'three': '3',
    'seven': '7',
    'eight': '8',
}

for line in f.readlines():
    newnum = ''

    for i, c in enumerate(line):
        check3 = i + 3
        check4 = i + 4
        check5 = i + 5

        if check3 <= len(line):
            if line[i:check3] in nums3:
                newnum = newnum + nums3[line[i:check3]]
        if check4 <= len(line):
            if line[i:check4] in nums4:
                newnum = newnum + nums4[line[i:check4]]
        if check5 <= len(line):
            if line[i:check5] in nums5:
                newnum = newnum + nums5[line[i:check5]]

        if c.isdigit():
            newnum = newnum + c

    print(newnum[0] + ' ' + newnum[-1])
    total = total + int(newnum[0] + newnum[-1])
print(total)