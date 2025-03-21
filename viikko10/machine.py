import math

def min_steps(x):
    if x == 1:
        return 0
    result = {}

    result[1] = 0
    for s in range(2, x + 1):
        if s - 3 in result:
            existing = result.get(s) or math.inf
            result[s] = min(result[s - 3] + 1, existing)
        if s % 2 == 0 and s // 2 in result:
            existing = result.get(s) or math.inf
            result[s] = min(result[s // 2] + 1, existing)
    return result.get(x) or -1


if __name__ == "__main__":
    print(min_steps(1))  # 0
    print(min_steps(2))  # 1
    print(min_steps(3))  # -1
    print(min_steps(4))  # 1
    print(min_steps(5))  # 2
    print(min_steps(17))  # 4
    print(min_steps(42))  # -1
    print(min_steps(100))  # 7
    print(min_steps(1000))  # 13
