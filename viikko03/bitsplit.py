def count_splits(sequence):
    if len(sequence) < 4:
        return 0

    l = [0, 0]
    r = [0, 0]
    c = 0

    for b in sequence[0:2]:
        b = int(b)
        l[b] += 1

    for b in sequence[2:]:
        b = int(b)
        r[b] += 1

    if l[0] == l[1] and r[0] == r[1]:
        c += 1

    for b in sequence[2:]:
        b = int(b)
        l[b] += 1
        r[b] -= 1

        if l[0] == l[1] and r[0] == r[1] and min(l) != 0 and min(r) != 0:
            c += 1

    return c


if __name__ == "__main__":
    print(count_splits("00"))  # 0
    print(count_splits("01"))  # 0
    print(count_splits("0110"))  # 1
    print(count_splits("010101"))  # 2
    print(count_splits("000111"))  # 0
    print(count_splits("01100110"))  # 3

    sequence = "01" * 10**5
    print(count_splits(sequence))  # 99999
