# https://cses.fi/tira25k/task/3537 

class FlipList:
    def __init__(self):
        # TODO

    def __repr__(self):
        # TODO

    def add_first(self, x):
        # TODO

    def add_last(self, x):
        # TODO

    def flip(self):
        # TODO

if __name__ == "__main__":
    numbers = FlipList()

    numbers.add_last(1)
    numbers.add_last(2)
    numbers.add_last(3)
    print(numbers) # [1, 2, 3]

    numbers.add_first(4)
    print(numbers) # [4, 1, 2, 3]

    numbers.flip()
    print(numbers) # [3, 2, 1, 4]

    numbers.add_last(5)
    print(numbers) # [3, 2, 1, 4, 5]
