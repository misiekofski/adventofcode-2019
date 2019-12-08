with open('8-input.txt') as fp:
    line = fp.readline()

layers = [line[i*150:(i+1)*150] for i in range(len(line)//150)]

less_zeros_layer = layers[0]

for i in range(len(layers)):
    if layers[i].count('0') < less_zeros_layer.count('0'):
        less_zeros_layer = layers[i]

print(less_zeros_layer.count('1') * less_zeros_layer.count('2'))

final_image = [int(s) for s in layers[0]]

# solution 8a
for i in range(100):
    temp_layer = [int(s) for s in layers[i]]
    for j in range(len(temp_layer)):
        if final_image[j] == 2 and temp_layer[j] != 2:
            final_image[j] = temp_layer[j]

print(final_image[:25])
print(final_image[25:50])
print(final_image[50:75])
print(final_image[75:100])
print(final_image[100:125])
print(final_image[125:150])


# print(final_image)
