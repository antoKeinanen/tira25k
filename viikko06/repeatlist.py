class RepeatList:
    def __init__(self):
        self.set = set()
        self.seen = False

    def append(self, number):
        if number in self.set:
            self.seen = True
        self.set.add(number)

    def repeat(self):
        return self.seen

if __name__ == "__main__":
    numbers = RepeatList()

    print(numbers.repeat()) # False

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.repeat()) # False

    numbers.append(2)
    print(numbers.repeat()) # True

    numbers.append(5)
    print(numbers.repeat()) # True