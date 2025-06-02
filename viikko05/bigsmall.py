def count_pairs(numbers):
    numbers = sorted(list(set(numbers)))
    used = set()

    for i, n in enumerate(numbers):
        for m in numbers[i:]:
            if n * 2 <= m:
                break
        else:
            break
        used.add(n)
        used.add(m)
    return len(used) // 2


if __name__ == "__main__":
    print(count_pairs([1]))  # 0
    print(count_pairs([1, 2, 3]))  # 1
    print(count_pairs([1, 2, 3, 4]))  # 2
    print(count_pairs([1, 1, 1, 1]))  # 0
    print(count_pairs([10**9, 1, 1, 1]))  # 1
    print(count_pairs([4, 5, 1, 4, 7, 8]))  # 2
    print(count_pairs([1, 2, 3, 2, 4, 6]))  # 3

    # numbers = [(x * 999983) % 10**6 + 1 for x in range(10**5)]
    # print(count_pairs(numbers))  # 41176
