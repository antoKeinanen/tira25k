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
        if a == b:
            return

        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]


class Components:
    def __init__(self, n):
        self.uf = UnionFind([i + 1 for i in range(n)])

    def add_road(self, a, b):
        self.uf.union(a, b)

    def count(self):
        nodes = self.uf.link.values()
        return sum(1 for node in nodes if node is None)


if __name__ == "__main__":
    components = Components(5)

    print(components.count())  # 5

    components.add_road(1, 2)
    components.add_road(1, 3)
    print(components.count())  # 3

    components.add_road(2, 3)
    print(components.count())  # 3

    components.add_road(4, 5)
    print(components.count())  # 2
