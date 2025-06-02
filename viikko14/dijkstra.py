import heapq
from timeit import default_timer as timer
from random import randint, shuffle


class Dijkstra:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))

    def find_distances(self, start_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0

        queue = []
        heapq.heappush(queue, (0, start_node))

        visited = set()
        while queue:
            node_a = heapq.heappop(queue)[1]
            if node_a in visited:
                continue
            visited.add(node_a)

            for node_b, weight in self.graph[node_a]:
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
                    new_pair = (new_distance, node_b)
                    heapq.heappush(queue, new_pair)

        return distances


if __name__ == "__main__":
    nodes = [i + 1 for i in range(5_000)]
    dijkstra = Dijkstra(nodes)

    for b in range(11, 5_001):
        for a in range(1, b + 1):
            if a < b and b - a < 10:
                dijkstra.add_edge(a, b, randint(1, 1_000))

    for edge in dijkstra.graph.values():
        shuffle(edge)


    print("Aloitetaan algoritmi")
    start = timer()
    dijkstra.find_distances(1)
    print("Valmis ajassa:", timer() - start)
