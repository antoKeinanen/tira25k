# https://cses.fi/tira25k/task/3569 

# hieman muutettu versio kurssimateriaalin luokasta
class MaximumFlow:
    # ...

    def construct(self, source, sink):
        self.flow = self.graph.copy()
        total = 0
        self.path_count = 0
        while True:
            self.seen = set()
            add = self.add_flow(source, sink, float("inf"))
            if add == 0:
                break
            total += add
            self.path_count += 1
        return total

def create_edges(x):
    # TODO

if __name__ == "__main__":
    edges = create_edges(42)

    maximum_flow = MaximumFlow(range(1, 100 + 1))

    for edge in edges:
        maximum_flow.add_edge(edge[0], edge[1], edge[2])

    maximum_flow.construct(1, 100)
    print(maximum_flow.path_count) # 42
