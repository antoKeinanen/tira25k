import re


def count_numbers(a, b):
    if a == b and re.match("^[25]+$", str(a)):
        return 1

    ub = len(str(b))+1
    c = 0
    for i in range(1, ub):
        for j in range(0, 2**i):
            n = int(bin(j)[2:].zfill(i).replace("0", "2").replace("1", "5"))
            if a <= n and n <= b:
                c += 1
    return c


if __name__ == "__main__":
    print(count_numbers(1, 100))  # 6
    print(count_numbers(60, 70))  # 0
    print(count_numbers(25, 25))  # 1
    print(count_numbers(1, 10**9))  # 1022
    print(count_numbers(123456789, 987654321))  # 512
