def find_sums(numbers, size):
    if size == 1:
        return numbers
    i, j = 0, size - 1
    b = []

    b.append(sum(numbers[i:j+1]))
    i += 1
    j += 1

    while j < len(numbers):
        prev = b[-1]
        prev_i = numbers[i - 1]
        prev_j = numbers[j]
        prev = prev - prev_i + prev_j
        b.append(prev)
        i += 1
        j += 1

    return b


if __name__ == "__main__":
    print(find_sums([1], 1))  # [1]
    print(find_sums([1, 8, 2, 7, 3, 6, 4, 5], 6))  # [27, 30, 27]

    print(find_sums([1, 2, 3, 4, 5], 1))  # [1, 2, 3, 4, 5]
    print(find_sums([1, 2, 3, 4, 5], 2))  # [3, 5, 7, 9]
    print(find_sums([1, 2, 3, 4, 5], 3))  # [6, 9, 12]
    print(find_sums([1, 2, 3, 4, 5], 4))  # [10, 14]
    print(find_sums([1, 2, 3, 4, 5], 5))  # [15]

    numbers = list(range(10**5))
    sums = find_sums(numbers, 10**4)
    print(sums[5])  # 50045000
    print(sums[42])  # 50415000
    print(sums[1337])  # 63365000
