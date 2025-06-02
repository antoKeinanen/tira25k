from math import ceil, sqrt
from heapq import heappush, heappop


def h(a, b):
    return abs(sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2))


def find_route(grid):
    a, b = (0, 0), (0, 0)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "A":
                a = (i, j)
            if grid[i][j] == "B":
                b = (i, j)

    open_list = []
    heappush(open_list, (h(a, b), a))

    closed_list = set()

    while len(open_list) > 0:
        cost, node = heappop(open_list)

        if node == b:
            return ceil(cost)

        if node in closed_list:
            continue

        closed_list.add(node)

        cost -= h(node, b)

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dir in dirs:
            i, j = node
            i -= dir[0]
            j -= dir[1]
            neighbor = (i, j)

            if grid[i][j] == "#":
                continue

            if neighbor in closed_list:
                continue

            neighbor_cost = cost + 1 + h(neighbor, b)
            heappush(open_list, (neighbor_cost, neighbor))

    return None


if __name__ == "__main__":
    grid = [
        "#########",
        "####..###",
        "#..##..B#",
        "#.#.#.#.#",
        "###.....#",
        "#..#.##.#",
        "#....#.##",
        "##A..##.#",
        "#########",
    ]
    print(find_route(grid))  # 9

    # grid = [
    #     "########",
    #     "#B#...A#",
    #     "#.#.##.#",
    #     "#......#",
    #     "########",
    # ]
    # print(find_route(grid))  # 9

    # grid = [
    #     "########",
    #     "####..B#",
    #     "#.A#.#.#",
    #     "#..#...#",
    #     "########",
    # ]
    # print(find_route(grid))  # None
