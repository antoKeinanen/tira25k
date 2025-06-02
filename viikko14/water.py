import heapq


class Dijkstra:
    def __init__(self):
        self.graph = {}
        self.nodes = []

    def add_node(self, node):
        self.graph[node] = []
        self.nodes.append(node)

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


def min_amount(left_volume, right_volume, target):
    queue = set()
    queue.add((0, 0))

    nodes = set()
    edges = set()

    while queue:
        node = queue.pop()
        nodes.add(node)
        l, r = node

        moves = [(l, 0), (l, right_volume), (0, r), (left_volume, r)]
        moves.append((l - r, min(r, right_volume)))
        moves.append((min(l, left_volume), r - l))

        for move in moves:
            edge = (node, move)     
            if edge not in edges:
                queue.add(move)
                edges.add((node, move))

    print(nodes)
    print(edges)


if __name__ == "__main__":
    print(min_amount(5, 4, 2))  # 22
    # print(min_amount(4, 3, 2))  # 16
    # print(min_amount(3, 3, 1))  # -1
    # print(min_amount(1, 1, 10**9))  # -1
    # print(min_amount(10, 9, 8))  # 46
    # print(min_amount(123, 456, 42))  # 10530
