def count_sublists(numbers):
    b = []
    c = 0
    s = 0
    p = None

    for n in numbers:
        if n % 2 != 0:
            x = c*(c + 1)/2
            b.append(x)
            c = 0
            s = 0
        else:
            c += 1
            if n == p:
                s += 1
        p = n

    x = c*(c + 1)/2
    b.append(x)

    return int(sum(b))


if __name__ == "__main__":
    print(count_sublists([7, 5, 1, 6, 10, 2, 8]))  # 10
    print(count_sublists([2, 4, 1, 6]))  # 4
    print(count_sublists([1, 2, 3, 4]))  # 2
    print(count_sublists([1, 1, 1, 1]))  # 0
    print(count_sublists([2, 2, 2, 2]))  # 10
    print(count_sublists([1, 1, 2, 1]))  # 1

    numbers = [2] * 10**5
    print(count_sublists(numbers))  # 5000050000
