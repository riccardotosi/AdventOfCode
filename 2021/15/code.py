def findNeighbors(node, i, j, data, visited_nodes):
    neighbors = []
    for r, c in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        if 0 <= r < len(data) and 0 <= c < len(data[i]) and not node in visited_nodes:
            neighbors.append((data[r][c], r, c))
    return neighbors

data = [[int(value) for value in line] for line in open('input.dat').read().splitlines()]
rows = len(data) ; columns = len(data[0])

# part 1
risk = {(r,c): 1e6 for r in range (0, len(data)) for c in range (0, len(data[r]))}
current_node = (0,0)
risk[current_node] = 0
visited_nodes = []
while not current_node == (rows-1, columns-1):
    i, j = current_node
    neighbors = findNeighbors(current_node, i, j, data, visited_nodes)
    for neighbor in neighbors:
        n_value, n_r, n_c = neighbor
        new_risk = risk[current_node] + n_value
        if new_risk < risk[(n_r, n_c)]:
            risk[(n_r, n_c)] = new_risk
    visited_nodes.append(current_node)
    new_step = min(risk.items(), key=lambda node: node[1] if not node[0] in visited_nodes else 1e6) # new node must be a non-visited node and the node that guarantees the minimum risk
    print(new_step)
    current_node = new_step[0]

print("Lowest total risk:", new_step[1])