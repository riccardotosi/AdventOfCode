data_raw=open("day2_input.dat").readlines()[0:]
data = [data_raw[i].split() for i in range (0,len(data_raw))]
for i in range (0,len(data)):
    data[i][1] = int(data[i][1])

# part 1

origin_v = 0
origin_h = 0

for i in range (0, len(data)):
    if data[i][0] == "forward":
        origin_h += data[i][1]
    elif data[i][0] == "down":
        origin_v += data[i][1]
    elif data[i][0] == "up":
        origin_v -= data[i][1]
    else:
        raise Exception("Movement not recognized.")

print("Answer:", origin_v*origin_h)

# answer 1660158

# part 2

origin_v = 0
origin_h = 0
aim = 0

for i in range (0, len(data)):
    if data[i][0] == "forward":
        origin_h += data[i][1]
        origin_v += data[i][1]*aim
    elif data[i][0] == "down":
        aim += data[i][1]
    elif data[i][0] == "up":
        aim -= data[i][1]
    else:
        raise Exception("Movement not recognized.")

print("Answer:", origin_v*origin_h)

# answer 1604592846