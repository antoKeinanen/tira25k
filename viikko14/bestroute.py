class BestRoute:
    def __init__(self, n):
        self.n = n
        self.nodes = [i+1 for i in range(n)]
        self.edges = []

    def add_road(self, a, b, x):
        self.edges.append((a, b, x))
        self.edges.append((b, a, x))
        
        

    def find_route(self, a, b):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[a] = 0
        previous = {}
        previous[a] = 0

        for _ in range(self.n - 1):
            for edge in self.edges:
                node_a, node_b, weight = edge
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
                    previous[node_b] = node_a
        
        return -1 if distances[b] == float("inf") else distances[b]


if __name__ == "__main__":
    routes = BestRoute(3)

    routes.add_road(1, 2, 2)
    print(routes.find_route(1, 3)) # -1

    routes.add_road(3, 1, 5)
    print(routes.find_route(1, 3)) # 5

    routes.add_road(2, 3, 1)
    print(routes.find_route(1, 3)) # 3
