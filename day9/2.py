from math import degrees
from itertools import combinations, pairwise
from functools import cache
# from rich import print, console

# import ipdb
# import IPython

from util import readlines, vec2, grid_set, display_grid, sliding_window, inputkind


def rect_area(c1: vec2, c2: vec2) -> int:
    return (abs(c1.x - c2.x) + 1) * (abs(c1.y - c2.y) + 1)


def in_rect(c1: vec2, c2: vec2, p: vec2) -> bool:
    xl, xh = sorted((c1.x, c2.x))
    yl, yh = sorted((c1.y, c2.y))
    return xl <= c2.x <= xh and yl <= p.y <= yh


def in_but_not_on_rect(c1: vec2, c2: vec2, p: vec2) -> bool:
    xl, xh = sorted((c1.x, c2.x))
    yl, yh = sorted((c1.y, c2.y))
    return xl < p.x < xh and yl < p.y < yh


# TODO: we can optimize orientation since all our line segments are axis-aligned


def vertical(line: tuple[vec2, vec2]) -> bool:
    a, b = line
    return a.x == b.x


def intersect(l1: tuple[vec2, vec2], l2: tuple[vec2, vec2], include_on=False) -> bool:
    o1 = vertical(l1)
    o2 = vertical(l2)
    if o1 == o2:
        return False
    if not o1:
        # l1 is horizontal
        y = l1[0].y
        yl = min(l2[0].y, l2[1].y)
        yh = max(l2[0].y, l2[1].y)
        x = l2[0].x
        xl = min(l1[0].x, l1[1].x)
        xh = max(l1[0].x, l1[1].x)
        if include_on:
            return yl <= y <= yh and xl <= x <= xh
        else:
            return yl < y < yh and xl < x < xh
    else:
        # l1 is vertical
        return intersect(l2, l1)


def orientation(p: vec2, q: vec2, r: vec2) -> int:
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or Counterclockwise


def doIntersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case: different orientations
    if o1 != 0 and o2 != 0 and o3 != 0 and o4 != 0 and o1 != o2 and o3 != o4:
        return True
    return False


red_tiles = [vec2(*map(int, line.split(","))) for line in readlines()]
red_tiles_set = set(red_tiles)

if inputkind() != "full":
    grid = [["." for _ in range(max(c.x for c in red_tiles) + 2)] for _ in range(max(c.y for c in red_tiles) + 2)]

max_x = max(c.x for c in red_tiles) + 1

polygon_edges = tuple(pairwise(red_tiles + [red_tiles[0]]))
polygon_edges_set = set(polygon_edges) | set((y, x) for (x, y) in polygon_edges)


# @cache
def on_line(line: tuple[vec2, vec2], p: vec2) -> bool:
    # optimization: the input edges are all axis-aligned
    if p in line:
        return True
    p1, p2 = line
    inbounds = (p1.x <= p.x <= p2.x) and (p1.y <= p.y <= p2.y)
    return inbounds
    v1p = p - p1
    v12 = p2 - p1
    zerocross = v1p.cross(v12) == 0
    return zerocross


def midpt(line: tuple[vec2, vec2]) -> vec2:
    return vec2((line[0].x + line[1].x) // 2, (line[0].y + line[1].y) // 2)


# @cache
def in_polygon(p: vec2):
    if p in red_tiles_set:
        return True
    # for edge in edges:
    #     if on_line(edge, p):
    #         return True  # on edge
    intersections = 0
    for dx in range(0, max_x + 1):
        for edge in polygon_edges:
            if on_line(edge, vec2(p.x + dx, p.y)):
                if dx == 0:
                    return True
                intersections += 1
    return intersections % 2 != 0


def normalize_angle(rad) -> int:
    return (int(degrees(rad)) + 360) % 360


def valid(c1, c2):
    c3 = vec2(c1.x, c2.y)
    c4 = vec2(c2.x, c1.y)
    flag = False
    for ep1, ep2 in polygon_edges:
        if in_but_not_on_rect(c1, c2, ep1) or in_but_not_on_rect(c1, c2, ep2):
            flag = True
            break
        if in_but_not_on_rect(c1, c2, midpt((ep1, ep2))):
            flag = True
            break
        for a, b in combinations((c1, c3, c2, c4), 2):
            if intersect((ep1, ep2), (a, b)):
                if area == 24:
                    print(f"intersect {ep1=} {ep2=} {a=} {b=}")
                flag = True
                break
        # if area == 40 and not flag:
        #     print(area)
        #     display_grid(grid, [ep1, ep2], [c1, c2, c3, c4])
        #     # IPython.embed(colors="neutral")
        #     try:
        #         i = input()
        #         if i == "s":
        #             IPython.embed(colors="neutral")
        #     except KeyboardInterrupt:
        #         raise SystemExit
        if flag:
            break
        # console.Console().clear()
        # intersects = in_rect(c1, c2, ep1) or in_rect(c1, c2, ep2)
        # if intersects:
        #     flag = True
        #     break
    return not flag


max_area = 0
n_checked = 0
n_skipped_too_small = 0
n_invalid = 0
try:
    for c1, c2 in combinations(red_tiles, 2):
        n_checked += 1
        if n_checked % 1000 == 0:
            print(n_checked)
        area = rect_area(c1, c2)
        if area <= max_area:
            n_skipped_too_small += 1
            continue
        if not valid(c1, c2):
            n_invalid += 1
            continue
        max_area = max(max_area, area)
except KeyboardInterrupt:
    print(max_area)
    print(f"{n_checked=} {n_skipped_too_small=} {n_invalid=}")

print(max_area)
