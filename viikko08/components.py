def find_components(nodes, edges):
    connections = {n: [] for n in nodes}
    for edge in edges:
        s, e = edge
        connections[s].append(e)
        connections[e].append(s)

    b = []
    visited = set([nodes[0]])
    total_visited = set(visited)
    stack = connections[nodes[0]]
    seen = len(visited)

    while seen < len(nodes):
        while len(stack) > 0:
            next = stack.pop()
            if next not in visited:
                stack.extend(connections[next])
                visited.add(next)
                total_visited.add(next)
                seen += 1
        b.append(sorted(list(visited)))
        visited = set()
        for node in nodes:
            if node not in total_visited:
                visited.add(node)
                total_visited.add(node)
                stack = connections[node]
                seen += 1
                break
    if len(visited) > 0:
        b.append(sorted(list(visited)))
    return sorted(b, key=lambda l: l[0])


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(find_components(nodes, edges))  # [[1, 2, 3], [4, 5, 6, 7], [8]]

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(find_components(nodes, edges))  # [[1], [2], [3], [4], [5]]

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(find_components(nodes, edges))  # [[1, 2, 3, 4, 5]]
