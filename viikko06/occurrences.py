class OccurrenceTracker:
    def __init__(self):
        self.seen = dict()
        self.counts = dict()
        self.seen_counts = 0

    def append(self, number):
        if number not in self.seen:
            self.seen[number] = 0
        self.seen[number] += 1

        n = self.seen[number]

        if n not in self.counts or self.counts[n] == 0:
            self.counts[n] = 0
            self.seen_counts += 1
        self.counts[n] += 1
        if n - 1 > 0:
            self.counts[n - 1] -= 1
            if not self.counts[n - 1] > 0:
                self.seen_counts -= 1

    def count(self):
        return self.seen_counts


if __name__ == "__main__":
    tracker = OccurrenceTracker()
    tracker.append(1)
    print(tracker.count())
    tracker.append(3)
    print(tracker.count())
    tracker.append(1)
    print(tracker.count())
