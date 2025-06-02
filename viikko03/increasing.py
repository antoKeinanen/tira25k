def count_sublists(numbers):
    b = []
    c = 0
    p = numbers[0]

    for n in numbers:
        if n > p:
            c += 1
        else:
            x = c * (c + 1) / 2
            b.append(x)
            c = 1
        p = n

    x = c * (c + 1) / 2
    b.append(x)

    return int(sum(b))


if __name__ == "__main__":
    print(count_sublists([2, 1, 3, 4]))  # 7
    print(count_sublists([1, 2, 3, 4]))  # 10
    print(count_sublists([4, 3, 2, 1]))  # 4
    print(count_sublists([1, 1, 1, 1]))  # 4
    print(count_sublists([1, 2, 1, 2]))  # 6

    numbers = list(range(1, 10**5 + 1))
    print(count_sublists(numbers))  # 5000050000
