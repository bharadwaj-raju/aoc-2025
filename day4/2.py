from collections.abc import Generator
from collections import deque

from util import readgrid, vec2, grid_get

grid = readgrid()


def roll_neighbors(grid, pos: vec2) -> Generator[vec2]:
    return (nb for nb in pos.all_neighbors() if grid_get(grid, nb) == "@")


def can_reach(grid, pos: vec2) -> bool:
    return len([*roll_neighbors(grid, pos)]) < 4


def get_reachable(grid) -> list[vec2]:
    reachable = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == ".":
                continue
            pos = vec2(x, y)
            if can_reach(grid, pos):
                reachable.append(pos)
    return reachable


def dig_deeper(grid, pos: vec2) -> set[vec2]:
    candidates = deque(roll_neighbors(grid, pos))

    grid[pos.y][pos.x] = "."
    removed = {pos}

    while candidates:
        c = candidates.popleft()
        if c in removed:
            continue
        if can_reach(grid, c):
            grid[c.y][c.x] = "."
            removed.add(c)
            candidates.extendleft(roll_neighbors(grid, c))

            # visualization:
            # from util import display_grid
            # display_grid(grid, candidates, [c])
            # input()
    return removed


all_removed = set()
initial_reachable = get_reachable(grid)
for r in initial_reachable:
    all_removed |= dig_deeper(grid, r)
print(len(all_removed))
