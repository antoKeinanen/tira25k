class AllPaths:
    def __init__(self, n):
        self.nodes = [i + 1 for i in range(n)]
        self.graph = {node: [] for node in self.nodes}

    def add_edge(self, a, b):
        self.graph[a].append(b)

    def count_from(self, node):
        if node in self.result:
            return self.result[node]

        path_count = 0
        for next_node in self.graph[node]:
            path_count += self.count_from(next_node)

        self.result[node] = path_count
        return path_count

    def count_paths(self, x, y):
        self.result = {y: 1}
        return self.count_from(x)

    def count(self):
        count = 0
        for node1 in self.nodes:
            for node2 in self.nodes:
                if node1 > node2:
                    continue
                count += self.count_paths(node1, node2)
        return count


if __name__ == "__main__":
    counter = AllPaths(4)

    counter.add_edge(1, 2)
    counter.add_edge(1, 3)
    counter.add_edge(2, 4)
    counter.add_edge(3, 4)

    print(counter.count())  # 10

    counter.add_edge(2, 3)

    print(counter.count())  # 14
