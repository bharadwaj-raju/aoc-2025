from util import readgrid, vec2, grid_get

grid = readgrid()

height, width = len(grid), len(grid[0])

reachable = 0
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == ".":
            continue
        pos = vec2(x, y)
        if len([nb for nb in pos.all_neighbors() if grid_get(grid, nb) == "@"]) < 4:
            reachable += 1
print(reachable)
