from dataclasses import dataclass
from ast import literal_eval
from itertools import chain, combinations


def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    Returns an iterator over all subsets of the given iterable.
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


from util import readlines


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


machines = []
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
    target = bits_to_num(machine.target)
    buttons = [bits_to_num(b) for b in machine.buttons]
    for combo in powerset(buttons):
        state = 0
        for b in combo:
            state ^= b
        if state == target:
            shortest.append(len(combo))
            break

print(sum(shortest))
