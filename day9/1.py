from itertools import combinations

from util import readlines, vec2


def rect_area(c1: vec2, c2: vec2) -> int:
    return (abs(c1.x - c2.x) + 1) * (abs(c1.y - c2.y) + 1)


red_tiles = [vec2(*map(int, line.split(","))) for line in readlines()]

print(max((rect_area(c1, c2), c1, c2) for c1, c2 in combinations(red_tiles, 2)))
