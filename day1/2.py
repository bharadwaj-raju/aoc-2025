from ..util import readlines

pos = 50
# pos2 = 50
nz = 0
# nz2 = 0

for line in readlines():
    dir, dist = line[0], int(line[1:])
    loops, actual = divmod(dist, 100)
    nz += loops
    if dir == "L":
        actual = -actual
    nextpos = (pos + actual) % 100
    if pos != 0 and actual < 0 and nextpos > pos:
        nz += 1
    elif pos != 0 and actual > 0 and nextpos < pos:
        nz += 1
    elif nextpos == 0:
        nz += 1
    pos = nextpos

    # for _ in range(dist):
    #     if dir == "L":
    #         pos2 -= 1
    #     else:
    #         pos2 += 1
    #     pos2 %= 100
    #     if pos2 == 0:
    #         nz2 += 1


print(nz)
