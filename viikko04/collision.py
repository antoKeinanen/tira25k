from string import ascii_letters
from random import choices

A = 23
M = 2**32


def hash_value(string):
    n = len(string)

    result = 0
    for i in range(n):
        code = ord(string[i]) - ord("a")
        result += code * A ** (n - i - 1)

    return result % M


def find_other(string):
    target = hash_value(string)
    s = ""

    while True:
        s += "b"
        if hash_value(s) == target:
            return s


if __name__ == "__main__":
    string1 = "kissa"
    string2 = find_other("kissa")
    print(string1, hash_value(string1))  # kissa 2905682
    print(string2, hash_value(string2))  # zfgjynuk 2905682
