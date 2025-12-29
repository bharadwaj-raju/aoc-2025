from functools import cache
from util import readlines


graph = {}
for line in readlines():
    src, dests = line.split(": ")
    graph[src] = []
    for dest in dests.split():
        graph[src].append(dest)


@cache
def npaths(src: str, dest: str) -> int:
    if src == dest:
        return 1
    n = 0
    for nb in graph.get(src, []):
        n += npaths(nb, dest)
    return n


print(
    npaths("svr", "fft") * npaths("fft", "dac") * npaths("dac", "out")
    + npaths("svr", "dac") * npaths("dac", "fft") * npaths("fft", "out")
)
