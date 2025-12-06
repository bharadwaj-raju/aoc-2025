from functools import reduce
from itertools import pairwise
from operator import add, mul

from util import readlines

lines = []
column_positions = []
ops = []
for line in readlines():
    if line.startswith(("+", "*")):
        spaces = 0
        for i, c in enumerate(line + "\n"):
            if c == "\n":
                column_positions.append(i)
            if c in "+*":
                column_positions.append(i - 1)
                ops.append(c)
                spaces = 0
            else:
                spaces += 1
    else:
        lines.append(line)

# print(column_positions)

transposed_problems = [[] for _ in range(len(ops))]
for line in lines:
    for i, (s, e) in enumerate(pairwise(column_positions)):
        transposed_problems[i].append(line[s + 1 : e])

problems = []
for t_prob in transposed_problems:
    prob = []
    for col in range(len(t_prob[0])):
        prob.append("".join(n[col] for n in t_prob))
    problems.append([int(x.strip()) for x in prob])

grand_total = 0
for nums, op in zip(problems, ops):
    fn, init = (add, 0) if op == "+" else (mul, 1)
    grand_total += reduce(fn, nums, init)
print(grand_total)
