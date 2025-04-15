# https://cses.fi/tira25k/task/3558 

class NewRoads:
    def __init__(self, n):
        # TODO

    def add_road(self, a, b, x):
        # TODO

    def min_cost(self):
        # TODO

if __name__ == "__main__":
    new_roads = NewRoads(4)

    new_roads.add_road(1, 2, 2)
    new_roads.add_road(1, 3, 5)
    print(new_roads.min_cost()) # -1

    new_roads.add_road(3, 4, 4)
    print(new_roads.min_cost()) # 11

    new_roads.add_road(2, 3, 1)
    print(new_roads.min_cost()) # 7
