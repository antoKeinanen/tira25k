# https://cses.fi/tira25k/task/3550 

class Connections:
    def __init__(self, n):
        # TODO

    def add_link(self, a, b):
        # TODO

    def check_network(self):
        # TODO

if __name__ == "__main__":
    connections = Connections(5)

    connections.add_link(1, 2)
    connections.add_link(2, 3)
    connections.add_link(1, 3)
    connections.add_link(4, 5)

    print(connections.check_network()) # False

    connections.add_link(3, 5)
    connections.add_link(1, 4)

    print(connections.check_network()) # False

    connections.add_link(5, 1)

    print(connections.check_network()) # True
