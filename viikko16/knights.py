class MaximumFlow:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {}
        for i in self.nodes:
            for j in self.nodes:
                self.graph[(i, j)] = 0

    def add_edge(self, node_a, node_b, capacity):
        self.graph[(node_a, node_b)] = capacity

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


class Ball:
    def __init__(self, nodes):
        self.mf = MaximumFlow(nodes)

    def add_pair(self, a, b):
        self.mf.add_edge(a, b, 1)
        self.mf.add_edge((-1, -1), a, 1)
        self.mf.add_edge(b, (-2, -2), 1)

    def max_pairs(self):
        return self.mf.construct((-1, -1), (-2, -2))


def parse(grid):
    n = len(grid)
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    nodes = set()
    edges = set()

    for i in range(n):
        for j in range(n):
            if grid[i][j] == "*":
                nodes.add((i, j))

                for dx, dy in moves:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == "*":
                        if (i, j) < (ni, nj):
                            edges.add(((i, j), (ni, nj)))

    return list(nodes), list(edges)


def count_pairs(grid):
    nodes, edges = parse(grid)
    nodes.extend([(-1, -1), (-2, -2)])
    ball = Ball(nodes)

    for edge in edges:
        ball.add_pair(*edge)

    return ball.max_pairs()


if __name__ == "__main__":
    grid = [
        "*.......",
        "..*...*.",
        "........",
        ".*......",
        "...*....",
        ".......*",
        "........",
        "......*.",
    ]

    print(count_pairs(grid))  # 3

    grid = [
        "*.***.**",
        "*******.",
        "*.**.**.",
        "***.****",
        "..****.*",
        "********",
        "*.******",
        "***.**.*",
    ]

    print(count_pairs(grid))  # 25
