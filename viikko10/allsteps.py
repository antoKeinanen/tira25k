def count_steps(x):
    if x == 1:
        return 1
    result = {}

    result[1] = 1
    for s in range(1, x + 1):
        if s - 3 in result:
            if s not in result:
                result[s] = 0
            result[s] += result[s-3]
        if s % 2 == 0 and s // 2 in result:
            if s not in result:
                result[s] = 0
            result[s] += result[s//2]
            
    return result.get(x) or 0

if __name__ == "__main__":
    print(count_steps(1)) # 1
    print(count_steps(2)) # 1
    print(count_steps(3)) # 0
    print(count_steps(4)) # 2
    print(count_steps(5)) # 1
    print(count_steps(17)) # 5
    print(count_steps(42)) # 0
    print(count_steps(100)) # 242
    print(count_steps(1000)) # 2948311