# https://cses.fi/tira25k/task/3543 

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1

class TreeSet:
    def __init__(self):
        self.root = None

    def add(self, value):
        # TODO

    def __contains__(self, value):
        # TODO

    def __repr__(self):
        # TODO

    def count(self, value):
        # TODO

if __name__ == "__main__":
    numbers = TreeSet()

    numbers.add(4)
    numbers.add(1)
    numbers.add(2)
    numbers.add(1)

    print(numbers) # [1, 1, 2, 4]

    print(1 in numbers) # True
    print(2 in numbers) # True
    print(3 in numbers) # False
    print(4 in numbers) # True

    print(numbers.count(1)) # 2
    print(numbers.count(2)) # 1
    print(numbers.count(3)) # 0
    print(numbers.count(4)) # 1
