"""Two herds of sea cucumbers sharing the same region:
- one always moves east (>),
- while the other always moves south (v).

Each location can contain at most one sea cucumber; the remaining locations are empty (.).

Every step,
- the sea cucumbers in the east-facing herd (>) attempt to move forward one location,
- then the sea cucumbers in the south-facing herd (v) attempt to move forward one location.

When a herd moves forward,
- every sea cucumber in the herd first simultaneously considers whether there is a sea cucumber
  in the adjacent location it's facing (even another sea cucumber facing the same direction),
- and then every sea cucumber facing an empty location simultaneously moves into that location.

- Sea cucumbers that move off the right edge of the map appear on the left edge,
- and sea cucumbers that move off the bottom edge of the map appear on the top edge.

Sea cucumbers always check whether their destination location is empty before moving, even if that destination is on the opposite side of the map

To find a safe place to land your submarine, the sea cucumbers need to stop moving

What is the first step on which no sea cucumbers move?"""

import copy

def pretty_print(map):
    for line in map:
        print(''.join(line))
    print()

def SeaCucumbersMovement(cucumbers_map):
    v_length = len(cucumbers_map) ; h_length = len(cucumbers_map[0])

    # horizontal moves
    h_cucumbers_map = copy.deepcopy(cucumbers_map)
    for i in range (0, h_length):
        ii = i + 1 if i < h_length - 1 else 0
        for j in range (0, v_length):
            jj = j
            if cucumbers_map[j][i] == ">" and cucumbers_map[jj][ii] == ".":
                h_cucumbers_map[j][i] = "."
                h_cucumbers_map[jj][ii] = ">"

    # vertical moves
    v_cucumbers_map = copy.deepcopy(h_cucumbers_map)
    for i in range (0, h_length):
        ii = i
        for j in range (0, v_length):
            jj = j + 1 if j < v_length - 1 else 0
            if h_cucumbers_map[j][i] == "v" and h_cucumbers_map[jj][ii] == ".":
                v_cucumbers_map[j][i] = "."
                v_cucumbers_map[jj][ii] = "v"

    return v_cucumbers_map

if __name__ == '__main__':

    lines_list = open('input.dat').read().splitlines()
    cucumbers_map = [[char for char in line] for line in lines_list]

    are_sea_cucumbers_moving = True
    it = 0
    while are_sea_cucumbers_moving:
        new_cucumbers_map = SeaCucumbersMovement(cucumbers_map)
        are_sea_cucumbers_moving = not(cucumbers_map == new_cucumbers_map)
        cucumbers_map = copy.deepcopy(new_cucumbers_map)
        it += 1

    print("First step on which no sea cucumbers move:", it)