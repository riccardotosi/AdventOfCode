import numpy as np

data = [[int(value) for value in line] for line in open('input.dat').read().splitlines()]
rows = len(data) ; columns = len(data[0])
skip_matrix = [[0 for _ in range (0, columns)] for _ in range (0, rows)]
risk_level = []
position_mins = []
for r in range (0, rows):
    for c in range (0, columns):
        if skip_matrix[r][c] == 0:
            value = data[r][c]
            is_min = []
            for (i, j) in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if i >= 0 and i < rows and j >= 0 and j < columns:
                    if value < data[i][j]:
                        is_min.append(True)
                        skip_matrix[i][j] = 1
                    else:
                        is_min.append(False)
            if all(is_min):
                risk_level.append(value+1)
                position_mins.append((r,c))
print("Risk level:", np.sum(risk_level))

basins  = [[] for _ in range (0, len(risk_level))]

def find_neighbors(value, r, c, basins, count):
    neighbors = [(data[i][j], i, j) for i, j in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)] if 0 <= i < rows and 0 <= j < columns and data[i][j] > value and not data[i][j]==9]
    for neighbor in neighbors:
        basins[count].append(neighbor)
        basins = find_neighbors(neighbor[0], neighbor[1], neighbor[2], basins, count)
    return basins

for count, (r, c) in enumerate(position_mins):
    basins[count].append((data[r][c], r, c))
    neighbors = find_neighbors(data[r][c], r, c, basins, count)
# remove duplicate tuples
basins = [list(set(basins[count])) for count in range (0, len(basins))]
lenghts = sorted([len(b) for b in basins])
print("Three largest basins and multiply their sizes together", lenghts[-1]*lenghts[-2]*lenghts[-3])