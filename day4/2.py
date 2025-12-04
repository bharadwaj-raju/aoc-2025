from util import readgrid, vec2, grid_get

grid = readgrid()


def can_reach(grid, pos: vec2) -> bool:
    return len([nb for nb in pos.all_neighbors() if grid_get(grid, nb, ".") == "@"]) < 4


def get_reachable(grid, only_check: set[vec2] | None = None) -> tuple[list[vec2], set[vec2]]:
    reachable = []
    neighbors = set()
    if only_check is None:
        only_check = {vec2(x, y) for y in range(len(grid)) for x in range(len(grid[0]))}
    for pos in only_check:
        cell = grid_get(grid, pos, ".")
        if cell == ".":
            continue
        if can_reach(grid, pos):
            reachable.append(pos)
            neighbors |= {nb for nb in pos.all_neighbors() if grid_get(grid, nb, ".") == "@"}
    return reachable, neighbors


all_removed = []
neighbors = None
while (removed_and_neighbors := get_reachable(grid, neighbors))[0]:
    now_removed, neighbors = removed_and_neighbors
    all_removed.extend(now_removed)
    for rm in now_removed:
        grid[rm.y][rm.x] = "."

print(len(all_removed))
