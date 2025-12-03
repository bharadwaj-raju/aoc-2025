from util import readlines

joltage_sum = 0
for line in readlines():
    joltages = [*map(int, line)]
    argmax = -1
    for i, x in enumerate(joltages):
        if argmax == -1 or joltages[argmax] < x:
            argmax = i
    d1 = joltages[argmax]
    try:
        d2 = max(joltages[argmax + 1 :])
    except ValueError:
        d2 = joltages[argmax]
        d1 = max(joltages[:argmax])
    joltage_sum += d1 * 10 + d2
print(joltage_sum)
