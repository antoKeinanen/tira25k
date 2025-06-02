class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreeSet:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        node = self.root
        while True:
            if node.value == value:
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    return
                node = node.right

    def remove(self, value):
        parent = None
        node = self.root

        while node and node.value != value:
            parent = node

            if node.value > value:
                node = node.left
            else:
                node = node.right

        if not node:
            return

        if node.left and node.right:
            successor_parent = node
            successor = node.right

            while successor.left:
                successor_parent = successor
                successor = successor.left

            node.value, successor.value = successor.value, node.value
            node = successor
            parent = successor_parent

        child = node.left if node.left else node.right
        if not parent:
            self.root = child
        elif not node.left and not node.right:
            if parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.right
        elif parent.left == node:
            parent.left = child
        else:
            parent.right = child

    def __repr__(self):
        items = []
        self.traverse(self.root, items)
        return str(items)

    def traverse(self, node, items):
        if not node:
            return
        self.traverse(node.left, items)
        items.append(node.value)
        self.traverse(node.right, items)


if __name__ == "__main__":
    numbers = TreeSet()

    numbers.add(3)
    numbers.remove(1)
    print(numbers) # [3]

    numbers.add(1)
    numbers.remove(4)
    print(numbers) # [1, 3]

    numbers.add(2)
    numbers.remove(1)
    print(numbers) # [2, 3]

    numbers.add(1)
    print(numbers) # [1, 2, 3]
