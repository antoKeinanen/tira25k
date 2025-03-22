import heapq


def find_boxes(boxes, products):
    boxes = sorted([(b, i) for i, b in enumerate(boxes)])
    products = sorted([(p, i) for i, p in enumerate(products)])

    used_boxes = set()

    result = [-1 for _ in products]
    for product, i in products:
        for box, j in boxes:
            if j in used_boxes:
                continue
            if product <= box:
                used_boxes.add(j)
                result[i] = box
                break
    
    return result



if __name__ == "__main__":
    print(find_boxes([4, 4, 6, 8], [5, 5, 4, 6, 1]))
    # [6, 8, 4, -1, 4]

    print(find_boxes([1, 2, 3, 4], [1, 1, 1, 1, 1]))
    # [1, 2, 3, 4, -1]

    print(find_boxes([2, 2, 2, 2], [1, 1, 1, 1, 1, 1]))
    # [2, 2, 2, 2, -1, -1]

    print(find_boxes([1, 1, 1, 1], [2, 2]))
    # [-1, -1]

    boxes = []
    products = []
    for i in range(10**5):
        boxes.append(i % 100 + 1)
        products.append(3 * i % 97 + 1)
    result = find_boxes(boxes, products)
    print(result[42])  # 30
    print(result[1337])  # 35
    print(result[-1])  # 100
