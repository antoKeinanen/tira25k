def can_win(numbers, p1, p2, p1_turn):
    if len(numbers) <= 1:
        if p1_turn:
            p1 += numbers[0]
        else:
            p1 += numbers[0]
        return p1 > p2

    first, last = numbers[0], numbers[-1]
    if p1_turn:
        return can_win(numbers[1:], p1 + first, p2, False) or can_win(
            numbers[:-1], p1 + last, p2, False
        )
    return can_win(numbers[1:], p1, p2+first, True) and can_win(
        numbers[:-1], p1, p2+last, True
    )


def first_wins(numbers):
    return can_win(numbers, 0, 0, True)


if __name__ == "__main__":
    print(first_wins([2, 1, 3]))  # True
    print(first_wins([1, 3, 1]))  # False

    print(first_wins([1]))  # True
    print(first_wins([1, 1]))  # False
    print(first_wins([1, 5]))  # True
    print(first_wins([1, 1, 1]))  # True
    print(first_wins([1, 2, 3, 4]))  # True
    print(first_wins([1, 3, 3, 7, 4, 2, 1]))  # False

    print(first_wins([1] * 50))  # False
    print(first_wins([1, 2] * 25))  # True
