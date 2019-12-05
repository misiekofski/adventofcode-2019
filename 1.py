result = 0

with open('input.txt') as fp:
    line = fp.readline()
    while line:
        result += (int(line)//3) - 2
        line = fp.readline()

print(str(result))
