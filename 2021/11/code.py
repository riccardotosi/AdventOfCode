"""Day 11
The energy level of each octopus is a value between 0 and 9.
You can model the energy levels and flashes of light in steps. During a single step, the following occurs:
    - First, the energy level of each octopus increases by 1.
    - Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, it also flashes. This process continues as long as new octopuses keep having their energy level increased beyond 9. (An octopus can only flash at most once per step.)
    - Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.
Observe that an adjacent flashes can cause an octopus to flash on a step even if it begins that step with very little energy.
"""

def pretty_print(map):
    for line in map:
        print(''.join(str(energy) + " " for energy in line))
    print()

if __name__ == "__main__":

    lines_list = open('input.dat').read().splitlines()
    octopus_map = [[int(energy) for energy in line] for line in lines_list]
    flashes_counter = 0
    for step in range (0,1000):
        flashes_step_counter = 0
        # energy level increases by 1
        for i in range (0, len(octopus_map)):
            for j in range (0, len(octopus_map[0])):
                octopus_map[i][j] += 1
        # octopuses with energy > 9 flash
        # and increase energy of adjacent octopuses (which are 8)
        # all octopuses that flashed restart from an energy = 0
        are_there_flashes = True
        while are_there_flashes:
            are_there_flashes = False
            for i in range (0, len(octopus_map)):
                for j in range (0, len(octopus_map[0])):
                    if octopus_map[i][j] > 9:
                        flashes_counter += 1
                        flashes_step_counter += 1
                        octopus_map[i][j] = 0
                        neighbors = [(i-1,j-1),(i-1,j),(i-1,j+1),
                            (i,j-1),(i,j+1),
                            (i+1,j-1),(i+1,j),(i+1,j+1)]
                        for m,n in neighbors:
                            if m >= 0 and m < len(octopus_map) and n >= 0 and n < len(octopus_map[0]) and octopus_map[m][n]:
                                octopus_map[m][n] += 1
                        are_there_flashes = True
        if flashes_step_counter == 100:
            break
    print("Number of flashes after 100 steps:", flashes_counter)
    print("Step with simultaneous flash of all octopuses:", step+1)