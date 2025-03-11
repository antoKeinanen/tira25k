class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"


def find(node, n):
    if node.value == n:
        return [node.value]
    for child in node.children:
        found = find(child, n)
        if found:
            return found + [node.value]
    return None


def find_path(node, a, b):
    a_path = find(node, a)
    b_path = find(node, b)

    if not a_path or not b_path:
        return None

    a_path = a_path[::-1]
    b_path = b_path[::-1]

    i = 1
    while i < len(a_path) and i < len(b_path) and a_path[i] == b_path[i]:
        i += 1

    return a_path[i:][::-1] + b_path[i-1:] 


if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]), Node(5), Node(2, [Node(6)])])
    print(find_path(tree1, 3, 2))  # [3, 4, 1, 2]
    print(find_path(tree1, 1, 7))  # [1, 4, 7]
    print(find_path(tree1, 5, 5))  # [5]
    print(find_path(tree1, 7, 3))  # [7, 4, 3]
    print(find_path(tree1, 4, 8))  # None

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(find_path(tree2, 1, 4))  # [1, 2, 3, 4]
    print(find_path(tree2, 4, 1))  # [4, 3, 2, 1]
    print(find_path(tree2, 2, 3))  # [2, 3]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(find_path(tree3, 2, 3))  # [2, 1, 3]
    print(find_path(tree3, 1, 2))  # [1, 2]
    print(find_path(tree3, 5, 5))  # None
