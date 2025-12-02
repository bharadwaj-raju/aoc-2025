from util import readtext

ranges = [[*map(int, r.split("-"))] for r in readtext().replace("\n", "").split(",")]


def made_of_two(n: int) -> bool:
    s = str(n)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]


idsum = 0
for r in ranges:
    for n in range(r[0], r[1] + 1):
        if made_of_two(n):
            idsum += n

print(idsum)
