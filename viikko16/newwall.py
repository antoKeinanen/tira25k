class MaximumFlow:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {}
        for i in self.nodes:
            for j in self.nodes:
                self.graph[(i, j)] = 0

    def add_edge(self, node_a, node_b, capacity):
        self.graph[(node_a, node_b)] += capacity

    def add_flow(self, node, sink, flow):
        if node in self.seen:
            return 0
        self.seen.add(node)
        if node == sink:
            return flow
        for next_node in self.nodes:
            if self.flow[(node, next_node)] > 0:
                new_flow = min(flow, self.flow[(node, next_node)])
                inc = self.add_flow(next_node, sink, new_flow)
                if inc > 0:
                    self.flow[(node, next_node)] -= inc
                    self.flow[(next_node, node)] += inc
                    return inc
        return 0

    def construct(self, source, sink):
        self.flow = self.graph.copy()
        total = 0
        while True:
            self.seen = set()
            add = self.add_flow(source, sink, float("inf"))
            if add == 0:
                break
            total += add
        return total


def parse(grid):
    nodes = []
    edges = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ".":
                nodes.append((i, j))

                if i + 1 < len(grid) and grid[i + 1][j] == ".":
                    edges.append(((i, j), (i + 1, j)))
                if j + 1 < len(grid[i]) and grid[i][j + 1] == ".":
                    edges.append(((i, j), (i, j + 1)))

    return nodes, edges


def min_changes(grid):
    nodes, edges = parse(grid)
    mf = MaximumFlow(nodes)

    for edge in edges:
        mf.add_edge(*edge, 1)

    source = (0, 0)
    sink = (len(grid) - 1, len(grid[-1]) - 1)

    return mf.construct(source, sink)


if __name__ == "__main__":
    grid = [
        "...#.",
        "...#.",
        "####.",
        ".....",
        ".....",
    ]

    print(min_changes(grid))  # 0

    grid = [
        ".#...",
        "...#.",
        "...#.",
        ".###.",
        ".###.",
    ]

    print(min_changes(grid))  # 0

    grid = [
        ".#...",
        "...#.",
        "...#.",
        ".###.",
        ".....",
    ]

    print(min_changes(grid))  # 1

    grid = [
        ".....",
        ".###.",
        "...#.",
        "##.#.",
        ".....",
    ]

    print(min_changes(grid))  # 2

    grid = [
        "..#",
        "...",
        "#..",
    ]
    print(min_changes(grid))  # 1
