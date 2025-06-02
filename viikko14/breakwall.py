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


def find_route(grid):
    dijkstra = Dijkstra()
    a = None
    b = None

    cost_by_char = {".": 0, "A": 0, "B": 0, "*": 1}
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            cell = grid[i][j]
            if cell != "#":
                node = (i, j)
                dijkstra.add_node(node)
                if cell == "A":
                    a = node
                elif cell == "B":
                    b = node

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "#":
                continue
            current_node = (i, j)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_i, new_j = i + dx, j + dy
                if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] != "#":
                    neighbor = (new_i, new_j)
                    weight = cost_by_char[grid[new_i][new_j]]
                    dijkstra.add_edge(current_node, neighbor, weight)

    distances = dijkstra.find_distances(a)
    return -1 if distances[b] == float("inf") else distances[b]


if __name__ == "__main__":
    grid = [
        "########",
        "#*A*...#",
        "#.*****#",
        "#.**.**#",
        "#.*****#",
        "#..*.B.#",
        "########",
    ]
    print(find_route(grid))  # 2
