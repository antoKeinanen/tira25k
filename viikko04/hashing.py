A = 23
M = 2**32


def hash_value(string):
    s = 0
    n = len(string)
    for i, c in enumerate(string):
        c = ord(c) - 97
        s += c * A ** (n - (i + 1))
    return s % M


if __name__ == "__main__":
    print(hash_value("abc"))  # 25
    print(hash_value("kissa"))  # 2905682
    print(hash_value("aybabtu"))  # 154753059
    print(hash_value("tira"))  # 235796
    print(hash_value("zzzzzzzzzz"))  # 2739360440
