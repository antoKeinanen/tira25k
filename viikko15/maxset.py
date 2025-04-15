# https://cses.fi/tira25k/task/3559 

class MaxSet:
    def __init__(self, n):
        # TODO

    def merge(self, a, b):
        # TODO

    def get_max(self):
        # TODO

if __name__ == "__main__":
    max_set = MaxSet(5)
    print(max_set.get_max()) # 1

    max_set.merge(1, 2)
    max_set.merge(3, 4)
    max_set.merge(3, 5)
    print(max_set.get_max()) # 3

    max_set.merge(1, 5)
    print(max_set.get_max()) # 5

    max_set.merge(2, 3)
    print(max_set.get_max()) # 5
