def calc_unique(seen):
    b = []
    for d in seen.values():
        b.extend(list(d))
    return len(set(b))


def analyze_route(grid: list[str]):
    d = "u"

    x = list(filter(lambda r: r.count("R"), grid))[0]
    y = grid.index(x)
    x = x.find("R")

    seen = {"u": set(), "l": set(), "d": set(), "r": set()}

    while True:
        if (x, y) in seen[d]:
            return (calc_unique(seen), False)
        seen[d].add((x, y))

        if d == "u":
            if not y - 1 >= 0:
                return (calc_unique(seen), True)
            if grid[y - 1][x] == "#":
                d = "r"
                continue
            y -= 1

        if d == "r":
            if x + 1 > len(grid[y]) - 1:
                return (calc_unique(seen), True)
            if grid[y][x + 1] == "#":
                d = "d"
                continue
            x += 1

        if d == "d":
            if y + 1 > len(grid) - 1:
                return (calc_unique(seen), True)
            if grid[y + 1][x] == "#":
                d = "l"
                continue
            y += 1

        if d == "l":
            if not x - 1 >= 0:
                return (calc_unique(seen), True)
            if grid[y][x - 1] == "#":
                d = "u"
                continue
            x -= 1


if __name__ == "__main__":
    grid1 = [".#......", "..#.....", ".......#", "#.R.....", "......#."]
    print(analyze_route(grid1))  # (14, True)

    grid2 = ["........", ".##.....", ".......#", "#.R.....", "......#."]
    print(analyze_route(grid2)) # (12, False)
