def count(weights, max_weight, weight, box_count):
    if not weights:
        return box_count
    c = float("inf")
    for product in weights:
        w = weights.copy()
        w.remove(product)

        if weight + product > max_weight:
            res = count(w, max_weight, product, box_count+1)
        else:
            res = count(w, max_weight, product+weight, box_count)
        c = min(res, c)
    return c

def min_count(weights, max_weight):
    if not weights:
        return 0
    if max(weights) > max_weight:
        return -1
    return count(weights, max_weight, 0, 1)


if __name__ == "__main__":
    print(min_count([2, 3, 3, 5], 7))  # 2
    print(min_count([2, 3, 3, 5], 6))  # 3
    print(min_count([2, 3, 3, 5], 5))  # 3
    print(min_count([2, 3, 3, 5], 4))  # -1

    print(min_count([], 1))  # 0
    print(min_count([1], 1))  # 1
    print(min_count([1, 1, 1, 1], 1))  # 4
    print(min_count([1, 1, 1, 1], 4))  # 1

    print(min_count([3, 4, 1, 2, 3, 3, 5, 9], 10))  # 3
