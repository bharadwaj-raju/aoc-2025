from ast import literal_eval
from dataclasses import dataclass
from itertools import chain, combinations

from z3 import IntVal, Optimize, Int

from util import readlines


def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    Returns an iterator over all subsets of the given iterable.
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def bits_to_num(bits: tuple[int]) -> int:
    n = 0
    for b in bits:
        n |= 1 << b
    return n


@dataclass
class Machine:
    target: tuple[int, ...]
    buttons: list[tuple[int, ...]]
    joltages: tuple[int, ...]


machines = list[Machine]()
for line in readlines():
    target = ()
    buttons = []
    joltages = ()
    for info in line.split():
        if info[0] == "[":
            info = info[1:-1]
            target = tuple(i for i, c in enumerate(info) if c == "#")
        elif info[0] == "(":
            buttons.append(literal_eval(info[:-1] + ",)"))
        elif info[0] == "{":
            joltages = literal_eval(info.replace("{", "(").replace("}", ",)"))
    machines.append(Machine(target, buttons, joltages))

shortest = []
for machine in machines:
    joltage_targets = list(machine.joltages)
    opt = Optimize()
    button_vars = [Int(f"b{i}") for i in range(len(machine.buttons))]
    for bv in button_vars:
        opt.add(bv >= 0)
    for joltage_idx, joltage in enumerate(machine.joltages):
        relevant = [
            button_vars[button_idx] for button_idx, button in enumerate(machine.buttons) if joltage_idx in button
        ]
        opt.add(sum(relevant, start=IntVal(0)) == joltage)
    # print(opt)
    h = opt.minimize(sum(button_vars, start=IntVal(0)))
    opt.check()
    n = opt.lower(h)
    print(opt.check(), n)
    shortest.append(n.as_long())

print(sum(shortest))
