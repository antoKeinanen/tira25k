class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __repr__(self):
        next = self.next
        s = f"{self.value} -> "
        while next != self:
            s += f"{next.value} -> "
            next = next.next
        s += "repeats"
        return s


def find_order(n):
    first = Node(1, None)
    prev = first
    for i in range(2, n+1):
        prev.next = Node(i, None)
        prev = prev.next
    prev.next = first

    b = []
    prev = first
    while len(b) < n:
        b.append(prev.next.value)
        prev.next = prev.next.next
        prev = prev.next
    return b



if __name__ == "__main__":
    print(find_order(1)) # [1]
    print(find_order(2)) # [2, 1]
    print(find_order(3)) # [2, 1, 3]
    print(find_order(7)) # [2, 4, 6, 1, 5, 3, 7]

    order = find_order(10**5)
    print(order[-5:]) # [52545, 85313, 36161, 3393, 68929]