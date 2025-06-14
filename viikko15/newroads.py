class UnionFind:
    def __init__(self, nodes):
        self.link = {node: None for node in nodes}
        self.size = {node: 1 for node in nodes}

    def find(self, x):
        while self.link[x]:
            x = self.link[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return

        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]


class Kruskal:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []

    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))

    def construct(self):
        self.edges.sort(key=lambda x: x[2])

        uf = UnionFind(self.nodes)
        edges_count = 0
        tree_weight = 0

        for edge in self.edges:
            node_a, node_b, weight = edge
            if uf.find(node_a) != uf.find(node_b):
                uf.union(node_a, node_b)
                edges_count += 1
                tree_weight += weight

        if edges_count != len(self.nodes) - 1:
            return None
        return tree_weight


class NewRoads:
    def __init__(self, n):
        self.kruskal = Kruskal([i+1 for i in range(n)])

    def add_road(self, a, b, x):
        self.kruskal.add_edge(a, b, x)

    def min_cost(self):
        return self.kruskal.construct() or -1

if __name__ == "__main__":
    new_roads = NewRoads(4)

    new_roads.add_road(1, 2, 2)
    new_roads.add_road(1, 3, 5)
    print(new_roads.min_cost()) # -1

    new_roads.add_road(3, 4, 4)
    print(new_roads.min_cost()) # 11

    new_roads.add_road(2, 3, 1)
    print(new_roads.min_cost()) # 7
