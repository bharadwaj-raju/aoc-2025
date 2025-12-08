from itertools import combinations
from rich import print

from util import readlines, vec3, inputkind


distances = {}

NSHORTEST = 1000 if inputkind() == "full" else 10

junctions = [vec3(*map(int, line.split(","))) for line in readlines()]

for a, b in combinations(junctions, 2):
    distances[a, b] = a.euclidean_square(b)

circuits = {j: {j} for j in junctions}

shortest_distances = sorted(distances, key=lambda pair: distances[pair], reverse=True)

a, b = None, None

while len(set(id(c) for c in circuits.values())) != 1:
    a, b = shortest_distances.pop()
    if circuits[a] is not circuits[b]:
        circuits[a].update(circuits[b])
        old_b_circuit = circuits[b]
        for j in circuits:
            if circuits[j] is old_b_circuit:
                circuits[j] = circuits[a]

assert a is not None
assert b is not None

print(a.x * b.x)
