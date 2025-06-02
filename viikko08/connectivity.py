def connected(nodes, edges):
    connections = {n: [] for n in nodes}
    for edge in edges:
        s, e = edge
        connections[s].append(e)
        connections[e].append(s)

    visited = set([nodes[0]])
    stack = connections[nodes[0]]

    while len(stack) > 0:
        next = stack.pop()
        if next not in visited:
            stack.extend(connections[next])
        visited.add(next)
    return len(visited) == len(nodes)


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 4), (4, 5)]
    print(connected(nodes, edges))  # True

    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(connected(nodes, edges))  # False

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(connected(nodes, edges))  # False

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(connected(nodes, edges))  # True
