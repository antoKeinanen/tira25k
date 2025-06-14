import heapq


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


def find_steps(numbers):
    n = len(numbers)
    nodes = range(len(numbers))
    dijkstra = Dijkstra(nodes)

    for i, number in enumerate(numbers):
        if not i + number > n - 1:
            dijkstra.add_edge(i, i + number, number)
        if not i - number < 0:
            dijkstra.add_edge(i, i - number, number)

    distances = dijkstra.find_distances(0)

    return -1 if distances[n - 1] == float("inf") else distances[n - 1]


if __name__ == "__main__":
    print(find_steps([1, 1, 1, 1]))  # 3
    print(find_steps([3, 2, 1]))  # -1
    print(find_steps([3, 5, 2, 2, 2, 3, 5]))  # 10
    print(find_steps([7, 5, 3, 1, 4, 2, 4, 6, 1]))  # 32

    numbers = []
    for i in range(10**5):
        numbers.append(1337 * i % 100 + 1)
    print(find_steps(numbers))  # 100055
