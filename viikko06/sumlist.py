class SumList:
    def __init__(self):
        self.list = [0]

    def append(self, number):
        n = self.list[-1]
        self.list.append(number + n)
            

    def sum(self, a, b):
        return self.list[b+1] - self.list[a]

if __name__ == "__main__":
    numbers = SumList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    numbers.append(4)
    numbers.append(5)

    print(numbers.sum(0, 4)) # 15
    print(numbers.sum(1, 1)) # 2
    print(numbers.sum(1, 3)) # 9
    print(numbers.sum(2, 3)) # 7
    print(numbers.sum(0, 3)) # 10

    numbers.append(1)
    print(numbers.sum(0, 5)) # 16
    print(numbers.sum(5, 5)) # 1