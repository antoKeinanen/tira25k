import heapq


def find_smallest(steps):
    heap = []
    seen = set()
    heapq.heappush(heap, 1)
    seen.add(1)

    for _ in range(steps):
        n = heapq.heappop(heap)
        seen.remove(n)
        a, b = n*2, n*3

        if a not in seen:
            seen.add(a)
            heapq.heappush(heap, a)
        if b not in seen:
            seen.add(b)
            heapq.heappush(heap, b)

    return heap[0]


if __name__ == "__main__":
    print(find_smallest(0))  # 1
    print(find_smallest(1))  # 2
    print(find_smallest(2))  # 3
    print(find_smallest(3))  # 4
    print(find_smallest(4))  # 6
    print(find_smallest(5))  # 8

    print(find_smallest(42))  # 1296
    print(find_smallest(1337))  # 16210220612075905068
    print(
        find_smallest(123123)
    )  # 47241633171870338440585357243035120029747450090811731814934867117962334088709324512562801224664331563355142646399182644605958987116029586018592281978123083613432358051028210559768563023872
