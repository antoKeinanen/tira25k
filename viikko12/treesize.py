# https://cses.fi/tira25k/task/3538 

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, value):
        # TODO

    def __len__(self):
        return self.size

if __name__ == "__main__":
    numbers = TreeSet()
    print(len(numbers)) # 0
    numbers.add(1)
    print(len(numbers)) # 1
    numbers.add(2)
    print(len(numbers)) # 2
    numbers.add(3)
    print(len(numbers)) # 3
    numbers.add(2)
    print(len(numbers)) # 3
