from util import readlines


def getbestnextdigit(n: str, digits_done: list[int]):
    # n is the *full string*
    # digits_done is a list of indices which were picked so far
    # we have to work with:
    try:
        offset = digits_done[-1] + 1
    except IndexError:
        # no digits chosen yet
        offset = 0
    digits_left = n[offset:]

    # if we need exactly as many digits as are left within the string
    # we don't need to think, just return the first
    digits_need = 12 - len(digits_done)
    if len(digits_left) == digits_need:
        return offset

    # if there are less digits to work with than we need... that shouldn't happen
    # we must have made a pick too far into the list earlier
    if len(digits_left) < digits_need:
        raise ValueError("we delved too greedily and too deep.")

    # now, we have the freedom to pick the highest number available
    # that does not reduce the remaining space to less than what we will need
    # in the future
    future_need = digits_need - 1
    available = digits_left[:-future_need] if future_need != 0 else digits_left[:]
    return max(list(enumerate(available)), key=lambda x: x[1])[0] + offset


joltage_sum = 0
for joltages in readlines():
    digits = []
    for _ in range(12):
        digits.append(getbestnextdigit(joltages, digits))
    final = "".join(str(joltages[i]) for i in digits)
    # print(final, len(final))
    joltage_sum += int(final)

print(joltage_sum)
