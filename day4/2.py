from util import readgrid, vec2, grid_get

grid = readgrid()


def get_reachable(grid) -> list[vec2]:
    reachable = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == ".":
                continue
            pos = vec2(x, y)
            if len([nb for nb in pos.all_neighbors() if grid_get(grid, nb, ".") == "@"]) < 4:
                reachable.append(pos)
    return reachable


all_removed = []
while now_removed := get_reachable(grid):
    all_removed.extend(now_removed)
    for rm in now_removed:
        grid[rm.y][rm.x] = "."

print(len(all_removed))
