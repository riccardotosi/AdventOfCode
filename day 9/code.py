import numpy as np

data = [[int(value) for value in line] for line in open('test.dat').read().splitlines()]
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

def search_basin(current, i, j, basin_path):
    neighbors = [(data[m][n], m, n) for m,n in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] \
                if 0 <= m < len(data) and 0 <= n < len(data[i]) \
                and data[m][n] > current and not data[m][n]==9]
    for neighbor in neighbors:
        basin_path.add((neighbor[0],neighbor[1], neighbor[2]))
        basin_path = search_basin(neighbor[0], neighbor[1], neighbor[2], basin_path)
    return basin_path

def find_neighbors(value, r, c):
    neighbors = [(i, j) for i, j in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)] if 0 <= i < rows and 0 <= j < columns and data[i][j] > value and not data[i][j]==9]
    print(neighbors)
    return neighbors

for count, (r, c) in enumerate(position_mins):
    basins[count].append(data[r][c])
    continuing = True
    while continuing:
        neighbors = find_neighbors(data[r][c], r, c)
        for neighbor in neighbors:
            basins[count].append(neighbor[0], neighbor[1])
            # look here for new neighbrs and values...

    # case up
    continuing = True
    (i, j) = (r-1, c)
    while continuing:
        if i >= 0 and i < rows and j >= 0 and j < columns:
            if data[i][j] >= data[i+1][j] and not data[i][j] == 9:
                basins[count].append((data[i][j],i,j))
            else:
                continuing = False
            i -= 1
        else:
            continuing = False
    # case down
    continuing = True
    (i, j) = (r+1, c)
    while continuing:
        if i >= 0 and i < rows and j >= 0 and j < columns:
            if data[i][j] >= data[i-1][j] and not data[i][j] == 9:
                basins[count].append((data[i][j],i,j))
            else:
                continuing = False
            i += 1
        else:
            continuing = False
    # case left
    continuing = True
    (i, j) = (r, c-1)
    while continuing:
        if i >= 0 and i < rows and j >= 0 and j < columns:
            if data[i][j] >= data[i][j+1] and not data[i][j] == 9:
                basins[count].append((data[i][j],i,j))
            else:
                continuing = False
            j -= 1
        else:
            continuing = False
    # case right
    continuing = True
    (i, j) = (r, c+1)
    while continuing:
        if i >= 0 and i < rows and j >= 0 and j < columns:
            if data[i][j] >= data[i][j+1] and not data[i][j] == 9:
                basins[count].append((data[i][j],i,j))
            else:
                continuing = False
            j += 1
        else:
            continuing = False
print(basins)