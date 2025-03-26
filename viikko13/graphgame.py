# https://cses.fi/tira25k/task/3549 

class GraphGame:
    def __init__(self, n):
        # TODO

    def add_link(self, a, b):
        # TODO

    def winning(self, x):
        # TODO

if __name__ == "__main__":
    game = GraphGame(6)

    game.add_link(3, 4)
    game.add_link(1, 4)
    game.add_link(4, 5)

    print(game.winning(3)) # False
    print(game.winning(1)) # False

    game.add_link(3, 1)
    game.add_link(4, 6)
    game.add_link(6, 5)

    print(game.winning(3)) # True
    print(game.winning(1)) # False
    print(game.winning(2)) # False
