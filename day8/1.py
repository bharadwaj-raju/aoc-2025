from math import prod
from itertools import combinations
from rich import print

from util import readlines, vec3, inputkind


distances = {}

NSHORTEST = 1000 if inputkind() == "full" else 10

junctions = [vec3(*map(int, line.split(","))) for line in readlines()]

for a, b in combinations(junctions, 2):
    distances[a, b] = a.euclidean_square(b)

circuits = {j: {j} for j in junctions}

shortest_distances = sorted(distances, key=lambda pair: distances[pair])[:NSHORTEST]

for a, b in shortest_distances:
    if circuits[a] is not circuits[b]:
        circuits[a].update(circuits[b])
        old_b_circuit = circuits[b]
        for j in circuits:
            if circuits[j] is old_b_circuit:
                circuits[j] = circuits[a]

circuits_by_size = sorted(circuits, key=lambda j: len(circuits[j]), reverse=True)
largest_circuit_ids = set()
largest_circuits = []
for j in circuits_by_size:
    circuit = circuits[j]
    if id(circuit) in largest_circuit_ids:
        continue
    largest_circuit_ids.add(id(circuit))
    largest_circuits.append(circuit)
    if len(largest_circuits) == 3:
        break

print(prod(map(len, largest_circuits)))
