from functools import reduce
from operator import add, mul

from util import readlines

problems = []
for line in readlines():
    row = line.split()
    if not problems:
        problems.extend([] for _ in range(len(row)))
    for i, c in enumerate(row):
        problems[i].append(c)

grand_total = 0
for i, problem in enumerate(problems):
    *nums, op = problem
    nums = [int(n) for n in nums]
    fn, init = (add, 0) if op == "+" else (mul, 1)
    result = reduce(fn, nums, init)
    grand_total += result
print(grand_total)
