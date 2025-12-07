from util import readgrid, vec2, grid_get, grid_set

grid = readgrid()

up = vec2(0, -1)
left = vec2(-1, 0)
right = vec2(+1, 0)

splitters_hit = set[vec2]()

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        pos = vec2(x, y)
        above = grid_get(grid, pos + up)
        if cell == "." and above in "S|":
            grid_set(grid, pos, "|")
        elif cell == "^" and above == "|":
            splitters_hit.add(pos)
            grid_set(grid, pos + left, "|")
            grid_set(grid, pos + right, "|")

print(len(splitters_hit))
