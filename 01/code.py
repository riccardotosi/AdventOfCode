data_day_1=open("day1_input.dat").readlines()[0:]

# part 1

previous_value = int(data_day_1[0])
counter = 0

for i in range (1, len(data_day_1)):
    current_value = int(data_day_1[i])
    if current_value > previous_value:
        counter += 1
    previous_value = current_value

print(counter)

# answer 1233

# part 2

previous_value = int(data_day_1[0])+int(data_day_1[1])+int(data_day_1[2])
counter = 0

for i in range (3, len(data_day_1)):
    current_value = int(data_day_1[i-2])+int(data_day_1[i-1])+int(data_day_1[i])
    if current_value > previous_value:
        counter += 1
    previous_value = current_value

print(counter)
