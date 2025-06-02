class MaxList:
    def __init__(self):
        self.max_num = 0

    def append(self, number):
        self.max_num = max(self.max_num, number)

    def max(self):
        return self.max_num

if __name__ == "__main__":
    numbers = MaxList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.max()) # 3

    numbers.append(8)
    numbers.append(5)
    print(numbers.max()) # 8