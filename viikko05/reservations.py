import random


def check_overlapping(reservations):
    reservations = sorted(reservations)
    for i in range(len(reservations) - 1):
        r = reservations[i]
        n = reservations[i + 1]
        if n[0] <= r[1]:
            return True
    return False


if __name__ == "__main__":
    print(check_overlapping([]))  # False
    print(check_overlapping([(1, 3)]))  # False
    print(check_overlapping([(4, 7), (1, 2)]))  # False
    print(check_overlapping([(4, 7), (1, 5)]))  # True
    print(check_overlapping([(1, 1), (2, 2)]))  # False
    print(check_overlapping([(1, 1), (1, 1)]))  # True
    print(check_overlapping([(2, 3), (5, 5), (3, 4)]))  # True
    print(check_overlapping([(2, 3), (5, 5), (1, 4)]))  # True
    print(check_overlapping([(2, 3), (5, 5), (1, 5)]))  # True

    reservations = [(day, day) for day in range(1, 10**5 + 1)]
    random.shuffle(reservations)
    print(check_overlapping(reservations))  # False

    reservations.append((42, 1337))
    random.shuffle(reservations)
    print(check_overlapping(reservations))  # True
