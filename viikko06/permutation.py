class PermutationTracker:
    def __init__(self):
        self.length = 0
        self.max = 0
        self.set = set()
        self.seen = False

    def append(self, number):
        if number in self.set:
            self.seen = True
        else:
            self.length += 1
            self.max = max(number, self.max)
        self.set.add(number)

    def check(self):
        if self.seen:
            return False
        if self.max != self.length:
            return False
        return True

if __name__ == "__main__":
    tracker = PermutationTracker()

    tracker.append(1)
    print(tracker.check()) # True

    tracker.append(4)
    print(tracker.check()) # False

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(3)
    print(tracker.check()) # True

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(5)
    print(tracker.check()) # False