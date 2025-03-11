def count_rooms(grid):
    connections = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ".":
                connections[(i, j)] = []
                if grid[i+1][j] == ".":
                    connections[(i, j)].append((i+1, j))
                if grid[i-1][j] == ".":
                    connections[(i, j)].append((i-1, j))
                if grid[i][j+1] == ".":
                    connections[(i, j)].append((i, j+1))
                if grid[i][j-1] == ".":
                    connections[(i, j)].append((i, j-1))
    
    b = []
    nodes = list(connections.keys())

    if len(nodes) == 0:
        return 0

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
        b.append(list(visited))
        visited = set()
        for node in nodes:
            if node not in total_visited:
                visited.add(node)
                total_visited.add(node)
                stack = connections[node]
                seen += 1
                break
    if len(visited) > 0:
        b.append(list(visited))
    return len(b)


if __name__ == "__main__":
    grid = ["########",
            "#.#..#.#",
            "#####..#",
            "#...#..#",
            "########"]
    print(count_rooms(grid)) # 4

    grid = ["########",
            "#......#",
            "#.####.#",
            "#......#",
            "########"]
    print(count_rooms(grid)) # 1

    grid = ["########",
            "######.#",
            "##.#####",
            "########",
            "########"]
    print(count_rooms(grid)) # 2 