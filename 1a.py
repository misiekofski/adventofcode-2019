result = 0


def get_fuel(fuel):
    temp = (fuel//3) - 2
    module_total = 0
    while temp > 0:
        module_total += temp
        temp = (temp//3) - 2
    return module_total


with open('input2.txt') as fp:
    line = fp.readline()
    while line:
        result += get_fuel(int(line))
        line = fp.readline()


print(result)
