from math import inf


def find_distances(street):
    l, r = -1, -1
    n = len(street)

    for i in range(n):
        if l == -1 and street[i] == "1":
            l = i
        if r == -1 and street[-(i + 1)] == "1":
            r = n - (i + 1)
        if l != -1 and r != -1:
            break

    lb = [inf for _ in range(n)]
    rb = [inf for _ in range(n)]
    for i in range(n):
        j = n - i - 1
        lb[i] = abs(i - l)
        rb[j] = abs(j - r)
        if street[i] == "1":
            l = i
            lb[i] = 0
        if street[j] == "1":
            r = j
            rb[j] = 0
    
    b = []
    for i in range(n):
        b.append(min(lb[i], rb[i]))


    return b


if __name__ == "__main__":
    print(find_distances("00100010"))  # [2, 1, 0, 1, 2, 1, 0, 1]
    print(find_distances("00100000"))  # [2, 1, 0, 1, 2, 3, 4, 5]
    print(find_distances("11111111"))  # [0, 0, 0, 0, 0, 0, 0, 0]
    print(find_distances("01010101"))  # [1, 0, 1, 0, 1, 0, 1, 0]
    print(find_distances("10000000"))  # [0, 1, 2, 3, 4, 5, 6, 7]
    print(find_distances("00000001"))  # [7, 6, 5, 4, 3, 2, 1, 0]

    n = 10**5
    street = "0" * n + "1" + "0" * n
    distances = find_distances(street)
    print(distances[1337])  # 98663
