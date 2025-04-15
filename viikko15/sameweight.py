# https://cses.fi/tira25k/task/3560 

class SameWeight:
    def __init__(self, n):
        # TODO

    def add_edge(self, a, b, x):
        # TODO

    def check(self):
        # TODO

if __name__ == "__main__":
    same_weight = SameWeight(4)

    same_weight.add_edge(1, 2, 2)
    same_weight.add_edge(1, 3, 3)
    print(same_weight.check()) # True

    same_weight.add_edge(1, 4, 3)
    print(same_weight.check()) # True

    same_weight.add_edge(3, 4, 3)
    print(same_weight.check()) # True

    same_weight.add_edge(2, 4, 1)
    print(same_weight.check()) # False
