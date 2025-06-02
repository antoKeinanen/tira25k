from random import shuffle
from timeit import default_timer as timer


def count_rounds_dict(numbers):
    n = len(numbers)

    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i

    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1

    return rounds


def count_rounds_list(numbers):
    n = len(numbers)

    pos = [0 for _ in range(n)]
    for i, x in enumerate(numbers):
        pos[x-1] = i

    rounds = 1
    for i in range(1, n):
        if pos[i] < pos[i-1]:
            rounds += 1

    return rounds


if __name__ == "__main__":
    nums = [i + 1 for i in range(10**7)]
    shuffle(nums)
    start_d = timer()
    count_rounds_dict(nums)
    print("Dict", timer() - start_d)

    start_l = timer()
    count_rounds_list(nums)
    print("List", timer() - start_l)
