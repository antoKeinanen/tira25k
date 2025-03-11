import random


def count_nested(intervals:list[tuple[int, int]]):
    intervals = sorted(intervals, key=lambda i: (i[0], -abs(i[1] - i[0])))
    i = 0
    j = 1
    c = 0
    while i < len(intervals) - 1:
        if j >= len(intervals):
            return c
        a = intervals[i]
        b = intervals[j]
        if a[0] <= b[0] and a[1] >= b[1]:
            c += 1
            j += 1
            continue
        i = j
        j = i + 1
    return c


if __name__ == "__main__":
    print(count_nested([(191, 257), (357, 568), (133, 394)]))  # 0
    print(count_nested([(1, 2)]))  # 0
    print(count_nested([(1, 2), (3, 4)]))  # 0
    print(count_nested([(1, 3), (2, 4)]))  # 0
    print(count_nested([(1, 4), (2, 3)]))  # 1
    print(count_nested([(1, 4), (1, 3)]))  # 1
    print(count_nested([(1, 4), (2, 4)]))  # 1
    print(count_nested([(1, 1), (1, 2), (1, 3)]))  # 2
    print(count_nested([(1, 6), (2, 5), (3, 4)]))  # 2
    print(count_nested([(1, 4), (2, 5), (3, 6)]))  # 0

    intervals = [(x+1, x+3) for x in range(10**5)]
    random.shuffle(intervals)
    print(count_nested(intervals)) # 0

    intervals = [(x+1, 2*10**5-x) for x in range(10**5)]
    random.shuffle(intervals)
    print(count_nested(intervals)) # 99999
