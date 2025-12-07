from functools import cache

from util import readgrid, vec2, grid_get

grid = readgrid()

down = vec2(0, +1)
left = vec2(-1, 0)
right = vec2(+1, 0)
downleft = down + left
downright = down + right


@cache
def get_timelines_after(beam_pos: vec2):
    while True:
        below = grid_get(grid, beam_pos + down, "#")
        if below == "#":
            return 1
        if below == ".":
            beam_pos += down
            continue
        if below == "^":
            return get_timelines_after(beam_pos + downleft) + get_timelines_after(beam_pos + downright)


start_pos = vec2(grid[0].index("S"), 0)
print(get_timelines_after(start_pos))
