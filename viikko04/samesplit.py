from collections import Counter


def count_splits(numbers):
    lc, rc = dict(), Counter(numbers)
    ls, rs = set(), set(numbers)

    c = 0

    for n in numbers:
        if not lc.get(n):
            lc[n] = 0

        lc[n] += 1
        rc[n] -= 1
        if n not in ls:
            ls.add(n)
        if not rc[n] > 0:
            rs.remove(n)

        if ls == rs:
            c += 1

    return c


if __name__ == "__main__":
    print(count_splits([1, 1, 1, 1]))  # 3
    print(count_splits([1, 1, 2, 1]))  # 0
    print(count_splits([1, 2, 1, 2]))  # 1
    print(count_splits([1, 2, 3, 4]))  # 0
    print(count_splits([1, 2, 1, 2, 1, 2]))  # 3

    numbers = [1, 2] * 10**5
    print(count_splits(numbers))  # 199997
    numbers = list(range(1, 10**5 + 1)) * 2
    print(count_splits(numbers))  # 1
