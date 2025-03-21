from itertools import combinations


def check_sum(numbers):
    n, m = 0, len(numbers)

    while n <= m:
        c1 = list(combinations(numbers, r=n))
        c2 = list(combinations(numbers, r=m))
        candidates = combinations(c1 + c2, r=2)
        for c in candidates:
            if sum(c[0]) == sum(c[1]):
                return True
        n += 1
        m -= 1
    return False


if __name__ == "__main__":
    print(check_sum([1, 2, 3, 4]))  # True
    print(check_sum([1, 2, 3, 5]))  # False
    print(check_sum([0]))  # True
    print(check_sum([2, 2]))  # True
    print(check_sum([2, 4]))  # False
    print(check_sum([1, 5, 6, 3, 5]))  # True
    print(check_sum([1, 5, 5, 3, 5]))  # False
    print(check_sum([10**9, 2 * 10**9, 10**9]))  # True
    print(check_sum([1, 1, 1, 1, 1, 1, 1, 1, 1, 123]))  # False
