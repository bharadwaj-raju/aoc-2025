from ..util import readlines

pos = 50
nz = 0
for line in readlines():
    dir, dist = line[0], int(line[1:])
    print(dir, dist)
    if dir == "L":
        dist = -dist
    pos = (pos + dist) % 100
    print(pos)
    print()
    if pos == 0:
        nz += 1
print(nz)
