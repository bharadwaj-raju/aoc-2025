from util import readtext

from functools import cache

ranges_raw = [
    [*map(int, r.split("-"))] for r in readtext().replace("\n", "").split(",")
]

# for the later loop we want all ranges to have a consistent number of digits
# I don't think the input has any ranges where the jump is more than one digit
# but we handle that anyway


@cache
def split_range(s: int, e: int) -> tuple[tuple[int, int], ...]:
    ls = len(str(s))
    le = len(str(e))
    if ls == le:
        return ((s, e),)
    if le - ls == 1:
        split = 10 ** (le - 1)
        return ((s, split - 1), (split, e))
    return ((s, (10**ls) - 1), *split_range(10**ls, e))


ranges = []
for s, e in ranges_raw:
    ranges.extend(split_range(s, e))


@cache
def repeaters(digits: int) -> list[int]:
    out = []
    for factor in range(1, digits):
        if digits % factor != 0:
            continue
        for pat in range(10 ** (factor - 1), 10**factor):
            rp = str(pat) * (digits // factor)
            if len(rp) == digits:
                out.append(int(rp))
    return out


ids = set()
for r in ranges:
    d = len(str(r[0]))
    for n in repeaters(d):
        if r[0] <= n <= r[1]:
            ids.add(n)

print(sum(ids))
