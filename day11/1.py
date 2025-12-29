from util import readlines

graph = {}
for line in readlines():
    src, dests = line.split(": ")
    graph[src] = set()
    for dest in dests.split():
        graph[src].add(dest)


def all_paths(graph: dict[str, set[str]], src: str, dest: str) -> list[list[str]]:
    paths = []
    current_path = []
    visited = set()

    def dfs(node):
        if node == dest:
            paths.append(current_path[:])
            return
        visited.add(node)
        for nb in graph[node]:
            if nb not in visited:
                current_path.append(nb)
                dfs(nb)
                current_path.pop()  # backtrack
        visited.remove(node)

    current_path.append(src)
    dfs(src)

    return paths


print(len(all_paths(graph, "you", "out")))
