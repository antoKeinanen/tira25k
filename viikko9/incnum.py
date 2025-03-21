def count_numbers(length, numbers, prefix=""):
    if length == 0:
        return 1
    if prefix.startswith("0"):
        return 0
    numbers = sorted([int(n) for n in numbers])
    c = 0
    for i in range(0, len(numbers)):
        c += count_numbers(length - 1, numbers[i:], f"{prefix}{numbers[i]}")
    return c


if __name__ == "__main__":
    print(count_numbers(3, "123"))  # 10
    print(count_numbers(5, "1"))  # 1
    print(count_numbers(2, "137"))  # 6
    print(count_numbers(8, "25689"))  # 495
    print(count_numbers(1, "0"))  # 1
    print(count_numbers(2, "0"))  # 0
    print(count_numbers(10, "12"))  # 11
    print(count_numbers(10, "123456789"))  # 43758
