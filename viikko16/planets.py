# https://cses.fi/tira25k/task/3564 

class Planets:
    def __init__(self, n):
        # TODO

    def add_teleport(self, a, b):
        # TODO

    def min_removals(self):
        # TODO

if __name__ == "__main__":
    planets = Planets(5)

    print(planets.min_removals()) # 0

    planets.add_teleport(1, 2)
    planets.add_teleport(2, 5)
    print(planets.min_removals()) # 1

    planets.add_teleport(1, 5)
    print(planets.min_removals()) # 2
