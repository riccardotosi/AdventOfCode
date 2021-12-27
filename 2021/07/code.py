positions =[int(pos) for pos in open('input.dat').read().splitlines()[0].split(',')]

fuels = []
for min_pos in range (min(positions),max(positions)+1):
    fuel = 0
    for pos in positions:
        fuel += abs(pos-min_pos)
    fuels.append(fuel)
print("Minumum fuel spent to align crab submarines burning fuel at a constant rate:", min(fuels))

fuels = []
for min_pos in range (min(positions),max(positions)+1):
    fuel = 0
    for pos in positions:
        fuel += abs(pos-min_pos)*(1+abs(min_pos-pos))/2
    fuels.append(fuel)
print("Minumum fuel spent to align crab submarines burning fuel at a non-constant rate:", int(min(fuels)))