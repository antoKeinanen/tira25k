from random import randint
from timeit import default_timer as timer


def find_mode_dict(numbers):
    count = {}
    mode = numbers[0]

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1

        if count[x] > count[mode]:
            mode = x

    return mode


def find_mode_sorted(numbers):
    numbers = sorted(numbers)
    n = numbers[0]
    c = 0
    max_c, max_n = 0, 0

    for x in numbers:
        if x == n:
            c += 1
        else:
            if c >= max_c:
                max_c = c
                max_n = n
            c = 0
        n = x
    if c >= max_c:
        max_c = c
        max_n = n
    return max_n


if __name__ == "__main__":
    lista = [randint(1, 1000) for _ in range(10**7)]
    print("Starting dict...")
    start = timer()
    res = find_mode_dict(lista)
    print("Endig dict", timer() - start, res)

    print("Starting sorted...")
    start = timer()
    res = find_mode_sorted(lista)
    print("Endig sorted", timer() - start, res)
