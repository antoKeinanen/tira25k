def create_string(pages):
    pages = list(sorted(set(pages)))
    s = ""
    n = pages[0]
    m = pages[0]
    b = True

    for p in pages[1:]:
        if b:
            if p == n + 1:
                n = p
            else:
                if m == n:
                    s += f"{n},"
                else:
                    s += f"{m}-{n},"
                m = p
                n = p
    if m == n:
        s += f"{n}"
    else:
        s += f"{m}-{n}"
    return s


if __name__ == "__main__":
    print(create_string([1]))  # 1
    print(create_string([13, 41]))  # 1
    print(create_string([1, 2, 3]))  # 1-3
    print(create_string([1, 1, 1]))  # 1
    print(create_string([1, 2, 1, 2]))  # 1-2
    print(create_string([1, 6, 2, 5]))  # 1-2,5-6
    print(create_string([1, 3, 5, 7]))  # 1,3,5,7
    print(create_string([1, 8, 2, 7, 3, 6, 4, 5]))  # 1-8
    print(create_string([3, 2, 9, 4, 3, 6, 9, 8]))  # 2-4,6,8-9

    pages = [3, 2, 1, 3, 2, 1]
    print(create_string(pages))  # 1-3
    print(pages)  # [3, 2, 1, 3, 2, 1]
