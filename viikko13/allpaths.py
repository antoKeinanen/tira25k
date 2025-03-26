# https://cses.fi/tira25k/task/3548 

class AllPaths:
    def __init__(self, n):
        # TODO

    def add_edge(self, a, b):
        # TODO

    def count(self):
        # TODO

if __name__ == "__main__":
    counter = AllPaths(4)

    counter.add_edge(1, 2)
    counter.add_edge(1, 3)
    counter.add_edge(2, 4)
    counter.add_edge(3, 4)

    print(counter.count()) # 10

    counter.add_edge(2, 3)

    print(counter.count()) # 14
