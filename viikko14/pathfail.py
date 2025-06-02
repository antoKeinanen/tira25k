import heapq

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

        print(distances)
        return distances


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

        print(distances)
        return distances


def create_edges(n, a, b):
    edges = [
        (1, n, b),
        (1, 2, 1),
        (2, 3, 0),
        (3, 1, 0),
    ]

    return edges


def find_answer(my_class, n, edges):
    nodes = range(1, n + 1)
    finder = my_class(nodes)

    for edge in edges:
        finder.add_edge(edge[0], edge[1], edge[2])

    distances = finder.find_distances(1)
    return distances[n]


if __name__ == "__main__":
    n = 100
    edges = create_edges(n, 42, 1337)

    answer1 = find_answer(BellmanFord, n, edges)
    print(answer1)  # 42

    answer2 = find_answer(Dijkstra, n, edges)
    print(answer2)  # 1337
