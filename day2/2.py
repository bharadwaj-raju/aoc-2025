from util import readtext

ranges = [[*map(int, r.split("-"))] for r in readtext().replace("\n", "").split(",")]


def made_of_patterns(n: int) -> bool:
    s = str(n)
    for factor in range(1, len(s)):
        if len(s) % factor == 0 and s == s[:factor] * (len(s) // factor):
            return True
    return False


idsum = 0
for r in ranges:
    for n in range(r[0], r[1] + 1):
        if made_of_patterns(n):
            idsum += n

print(idsum)
