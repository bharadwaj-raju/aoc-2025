from itertools import pairwise

from util import readgroups

fresh_ranges, available = readgroups()

fresh_ranges = [list(map(int, line.split("-"))) for line in fresh_ranges]
available = {int(a) for a in available}

fresh_ranges.sort()

if len(fresh_ranges) < 100:
    print(fresh_ranges)

# make disjoint
for r1, r2 in pairwise(fresh_ranges):
    (a1, b1), (a2, b2) = r1, r2
    # by virtue of sorting, a1 <= a2
    # so if b1 >= a2, there is some overlap
    # we can make them disjoint by setting a2 = b1+1
    if b1 >= a2:
        r2[0] = b1 + 1
    # but consider also:
    # 1-10, 4-5, 6-7
    # ((1, 10), (4, 5)) makes (4, 5) into (11, 5), invalidating it
    # but next iter:
    # ((11, 5), (6, 7)) -- no change even though (6, 7) should also be invalidated
    # so we make sure to propagate the highest end-value using invalidated ranges
    if a1 > b1 and a1 > r2[0]:
        r2[0] = a1

if len(fresh_ranges) < 100:
    print(fresh_ranges)

freshcount = 0
for fr in fresh_ranges:
    a, b = fr
    freshcount += len(range(a, b + 1))
print(freshcount)
