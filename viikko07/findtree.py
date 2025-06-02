class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"


def find_root(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != ".":
                return (i, j)


def find_tree(grid: list[list[str]]):
    ri, rj = find_root(grid)
    root = Node(int(grid[ri][rj]), [None, None, None])
    queue = []
    i, j = ri, rj

    while i + 1 < len(grid) and j - 1 >= 0 and grid[i + 1][j - 1] == "/":
        i += 1
        j -= 1
    if i + 1 < len(grid) and j - 1 >= 0 and grid[i + 1][j - 1] != ".":
        queue.append((i + 1, j - 1, root, "l"))

    i, j = ri, rj
    while i + 1 < len(grid) and grid[i + 1][j] == "|":
        i += 1
    if i + 1 < len(grid) and grid[i + 1][j] != ".":
        queue.append((i + 1, j, root, "d"))

    i, j = ri, rj
    while i + 1 < len(grid) and j + 1 < len(grid[i]) and grid[i + 1][j + 1] == "\\":
        i += 1
        j += 1
    if i + 1 < len(grid) and j + 1 < len(grid[i]) and grid[i + 1][j + 1] != ".":
        queue.append((i + 1, j + 1, root, "r"))

    while len(queue) > 0:
        ni, nj, parent, d = queue.pop()
        node = Node(int(grid[ni][nj]), [None, None, None])

        if d == "l":
            parent.children[0] = node
        if d == "d":
            parent.children[1] = node
        if d == "r":
            parent.children[2] = node

        incremented = False
        i, j = ni, nj
        while i + 1 < len(grid) and j - 1 >= 0 and grid[i + 1][j - 1] == "/":
            i += 1
            j -= 1
            incremented = True
        if (
            i + 1 < len(grid)
            and j - 1 >= 0
            and grid[i + 1][j - 1] != "."
            and incremented
        ):
            queue.append((i + 1, j - 1, node, "l"))

        incremented = False
        i, j = ni, nj
        while i + 1 < len(grid) and grid[i + 1][j] == "|":
            i += 1
            incremented = True
        if i + 1 < len(grid) and grid[i + 1][j] != "." and incremented:
            queue.append((i + 1, j, node, "d"))

        incremented = False
        i, j = ni, nj
        while i + 1 < len(grid) and j + 1 < len(grid[i]) and grid[i + 1][j + 1] == "\\":
            i += 1
            j += 1
            incremented = True
        if (
            i + 1 < len(grid)
            and j + 1 < len(grid[i])
            and grid[i + 1][j + 1] != "."
            and incremented
        ):
            queue.append((i + 1, j + 1, node, "r"))
    
    queue = [root]
    while len(queue) > 0:
        node = queue.pop()
        node.children = list(filter(lambda n: n is not None, node.children))
        queue.extend(node.children)

    return root


if __name__ == "__main__":
    grid = [
        ".....",
        "..3..",
        "./|\.",
        "2.|.4",
        "..1..",
    ]
    print(find_tree(grid))
    exit()
    grid = [
        "...........",
        "...........",
        "......5....",
        "...../.\...",
        "....3...\..",
        "....|....1.",
        "....2......",
    ]
    tree = find_tree(grid)
    print(tree)
    # Node(5, [Node(3, [Node(2)]), Node(1)])

    grid = [
        "....1.....",
        ".../.\....",
        "..2...\...",
        "..|....3..",
        "..7.../|\.",
        "./.\.4.5.6",
        "8...9.....",
    ]
    tree = find_tree(grid)
    print(tree)
    # Node(1, [Node(2, [Node(7, [Node(8), Node(9)])]), Node(3, [Node(4), Node(5), Node(6)])])
