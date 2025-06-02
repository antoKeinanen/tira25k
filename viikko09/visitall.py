import itertools
import math


def get_distance(distances, route):
    length = 0
    current = 1
    for next in route[1:]:
        length += distances[next-1][current-1]
        current = next
    return length


def find_route(distances):
    candidates = itertools.permutations(
        range(2, len(distances) + 1), len(distances) - 1
    )
    candidates = [list(c) for c in candidates]
    length, route = math.inf, []

    for candidate in candidates:
        candidate = [1] + candidate + [1]
        cl = get_distance(distances, candidate)
        if cl < length:
            length, route = cl, candidate

    return length, route


if __name__ == "__main__":
    distances = [
        [9, 3],
        [3, 6],
    ]
    length, route = find_route(distances)
    print(length) # 9
    print(route) # [1, 3, 5, 2, 4, 1]

    distances = [[0, 2, 2, 1, 8],
                 [2, 0, 9, 1, 2],
                 [2, 9, 0, 8, 3],
                 [1, 1, 8, 0, 3],
                 [8, 2, 3, 3, 0]]

    length, route = find_route(distances)
    print(length) # 9
    print(route) # [1, 3, 5, 2, 4, 1]

    distances = [[0, 7, 5, 9, 6, 3, 1, 3],
                 [7, 0, 3, 2, 3, 3, 7, 8],
                 [5, 3, 0, 4, 2, 7, 7, 1],
                 [9, 2, 4, 0, 2, 3, 2, 4],
                 [6, 3, 2, 2, 0, 9, 5, 9],
                 [3, 3, 7, 3, 9, 0, 4, 5],
                 [1, 7, 7, 2, 5, 4, 0, 7],
                 [3, 8, 1, 4, 9, 5, 7, 0]]

    length, route = find_route(distances)
    print(length) # 18
    print(route) # [1, 7, 4, 6, 2, 5, 3, 8, 1]
