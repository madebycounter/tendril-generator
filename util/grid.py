def grid_neighbors(grid, cell):
    x, y = cell
    neighbors = []

    def check(x, y):
        try:
            return grid[x][y]
        except IndexError:
            return 0

    to_check = [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]

    for neighbor in to_check:
        if check(*neighbor):
            neighbors.append(neighbor)

    return neighbors
