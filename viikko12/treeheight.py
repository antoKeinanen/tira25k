# https://cses.fi/tira25k/task/3539 

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None
        self.max_depth = -1

    def add(self, value):
        # TODO

    def height(self):
        return self.max_depth

if __name__ == "__main__":
    numbers = TreeSet()
    print(numbers.height()) # -1
    numbers.add(2)
    print(numbers.height()) # 0
    numbers.add(1)
    print(numbers.height()) # 1
    numbers.add(3)
    print(numbers.height()) # 1
    numbers.add(4)
    print(numbers.height()) # 2
