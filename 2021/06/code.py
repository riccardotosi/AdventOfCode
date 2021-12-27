# each lanternfish creates a new lanternfish once every 7 days
# this process isn't necessarily synchronized between every lanternfish --> model each fish as a single number that represents the number of days until it creates a new lanternfish
# a new lanternfish would surely need slightly longer before it's capable of producing more lanternfish: two more days for its first cycle
import time

class Lanternfish:
    def __init__(self, internal_timer):
        self.internal_timer = internal_timer

def simulateLife(days, fishes):
    for day in range (0, days):
        new_fishes = 0
        for fish in fishes:
            if fish.internal_timer == 0:
                fish.internal_timer = 6
                new_fishes += 1
            else:
                fish.internal_timer += -1
        for _ in range (0, new_fishes):
            fishes.append(Lanternfish(internal_timer=8))
    return fishes

def simulateLifeEfficiently(days, fishes_dict):
    for day in range (0, days):
        new_fishes_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for key, value in fishes_dict.items():
            if key == 0:
                new_fishes_dict[8] += value
                new_fishes_dict[6] += value
            elif key > 0:
                new_fishes_dict[key-1] += value
        fishes_dict = new_fishes_dict
    return fishes_dict

data = open('input.dat', 'r').read().splitlines()[0].split(",")
fishes = []
for timer in data:
    fishes.append(Lanternfish(internal_timer=int(timer)))
fishes = simulateLife(80, fishes)
print("Number of lanternfish after 80 days:",len(fishes))

fishes_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
fishes = []
for timer in data:
    fishes_dict[int(timer)] += 1
fishes_dict = simulateLifeEfficiently(256, fishes_dict)
print("Number of lanternfish after 256 days:",sum(fishes_dict.values()))