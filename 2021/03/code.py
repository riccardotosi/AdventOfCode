data_raw = [line for line in open('day3_input.dat', 'r').read().splitlines()]
data = []
for i in range (0, len(data_raw[0])):
    data.append([data_line[i] for data_line in data_raw])
g = [max(value, key=value.count) for value in data] ; g = "".join(g)
e = [min(value, key=value.count) for value in data] ; e = "".join(e)
print("Power consumption of the submarine =", int(g,2)*int(e,2))