# https://cses.fi/tira25k/task/3557 

class Components:
    def __init__(self, n):
        # TODO

    def add_road(self, a, b):
        # TODO

    def count(self):
        # TODO

if __name__ == "__main__":
    components = Components(5)

    print(components.count()) # 5

    components.add_road(1, 2)
    components.add_road(1, 3)
    print(components.count()) # 3

    components.add_road(2, 3)
    print(components.count()) # 3

    components.add_road(4, 5)
    print(components.count()) # 2
