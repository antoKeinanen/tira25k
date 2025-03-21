from itertools import chain, combinations

def count_combinations(cards, target):
    candidates = chain.from_iterable(combinations(cards, r) for r in range(len(cards)+1))
    return len([1 for c in candidates if sum(c) == target]) 

if __name__ == "__main__":
    print(count_combinations([2, 1, 4, 6], 6)) # 2
    print(count_combinations([1, 1, 1, 1], 2)) # 6
    print(count_combinations([2, 1, 4, 6], 15)) # 0
    print(count_combinations([1], 1)) # 1
    print(count_combinations([1, 2, 3, 4, 5], 5)) # 3
    print(count_combinations([1, 1, 4, 1, 1], 4)) # 2
    print(count_combinations([1] * 10, 5)) # 252