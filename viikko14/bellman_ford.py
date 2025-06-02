from timeit import default_timer as timer
from random import randint, shuffle


class BellmanFord:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []

    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))

    def find_distances(self, start_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0

        num_rounds = len(self.nodes) - 1
        for _ in range(num_rounds):
            for edge in self.edges:
                node_a, node_b, weight = edge
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance

        return distances


if __name__ == "__main__":
    nodes = [i + 1 for i in range(5_000)]
    bellman_ford = BellmanFord(nodes)

    for b in range(5_001):
        for a in range(1, b + 1):
            if a < b and b - a < 10:
                bellman_ford.add_edge(a, b, randint(1, 1_000))

    shuffle(bellman_ford.edges)

    print("Aloitetaan algoritmi")
    start = timer()
    bellman_ford.find_distances(0)
    print("Valmis ajassa:", timer() - start)
