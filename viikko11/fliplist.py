from collections import deque


class FlipList:
    def __init__(self):
        self.flipped = False
        self.list = deque()

    def __repr__(self):
        if self.flipped:
            lista = list(self.list)[::-1]
        else:
            lista = list(self.list)

        return str(lista)

    def add_first(self, x):
        if self.flipped:
            self.list.append(x)
        else:
            self.list.appendleft(x)

    def add_last(self, x):
        if self.flipped:
            self.list.appendleft(x)
        else:
            self.list.append(x)

    def flip(self):
        self.flipped = not self.flipped


if __name__ == "__main__":
    numbers = FlipList()

    numbers.add_last(1)
    numbers.add_last(2)
    numbers.add_last(3)
    print(numbers)  # [1, 2, 3]

    numbers.add_first(4)
    print(numbers)  # [4, 1, 2, 3]

    numbers.flip()
    print(numbers)  # [3, 2, 1, 4]

    numbers.add_last(5)
    print(numbers)  # [3, 2, 1, 4, 5]
