from functools import reduce

from util import readgroups

fresh_ranges, available = readgroups()

fresh_ranges = [tuple(map(int, line.split("-"))) for line in fresh_ranges]
available = {int(a) for a in available}
fresh_ranges = [range(fr[0], fr[1] + 1) for fr in fresh_ranges]

# fresh = {i for fr in fresh_ranges for i in range(fr[0], fr[1] + 1)}

freshcount = 0
for a in available:
    for fr in fresh_ranges:
        if a in fr:
            freshcount += 1
            break
print(freshcount)
