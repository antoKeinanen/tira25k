# https://cses.fi/tira25k/task/3551 

class BestRoute:
    def __init__(self, n):
        # TODO

    def add_road(self, a, b, x):
        # TODO

    def find_route(self, a, b):
        # TODO

if __name__ == "__main__":
    routes = BestRoute(3)

    routes.add_road(1, 2, 2)
    print(routes.find_route(1, 3)) # -1

    routes.add_road(3, 1, 5)
    print(routes.find_route(1, 3)) # 5

    routes.add_road(2, 3, 1)
    print(routes.find_route(1, 3)) # 3
