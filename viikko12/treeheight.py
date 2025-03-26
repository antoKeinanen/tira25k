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
        if not self.root:
            self.root = Node(value)
            self.max_depth = 0
            return

        depth = 0
        node = self.root
        while True:
            if node.value == value:
                return
            if node.value > value:
                depth += 1
                if not node.left:
                    node.left = Node(value)
                    self.max_depth = max(depth, self.max_depth)
                    return
                node = node.left
            else:
                depth += 1
                if not node.right:
                    node.right = Node(value)
                    self.max_depth = max(depth, self.max_depth)
                    return
                node = node.right

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
