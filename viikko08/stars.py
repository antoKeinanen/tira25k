def parse(grid):
    stars = {}

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "*":
                stars[(i, j)] = []
                if i + 1 < len(grid) and grid[i + 1][j] == "*":
                    stars[(i, j)].append((i + 1, j))
                if i - 1 >= 0 and grid[i - 1][j] == "*":
                    stars[(i, j)].append((i - 1, j))
                if j + 1 < len(grid[i]) and grid[i][j + 1] == "*":
                    stars[(i, j)].append((i, j + 1))
                if j - 1 >= 0 and grid[i][j - 1] == "*":
                    stars[(i, j)].append((i, j - 1))
                if (
                    i + 1 < len(grid)
                    and j + 1 < len(grid[i])
                    and grid[i + 1][j + 1] == "*"
                ):
                    stars[(i, j)].append((i + 1, j + 1))
                if i - 1 >= 0 and j + 1 < len(grid[i]) and grid[i - 1][j + 1] == "*":
                    stars[(i, j)].append((i - 1, j + 1))
                if i + 1 < len(grid) and j - 1 >= 0 and grid[i + 1][j - 1] == "*":
                    stars[(i, j)].append((i + 1, j - 1))
                if i - 1 >= 0 and j - 1 >= 0 and grid[i - 1][j - 1] == "*":
                    stars[(i, j)].append((i - 1, j - 1))
    return stars


def detect_patterns(stars):
    seen = set()
    patterns_buf = []

    for star in stars:
        if star in seen:
            continue
        b = []
        queue = [star]
        while len(queue) > 0:
            s = queue.pop()
            if s in seen:
                continue
            seen.add(s)
            b.append(s)
            for st in stars[s]:
                if st not in seen:
                    queue.append(st)
        patterns_buf.append(b)
    return patterns_buf


def compute_bounds(pattern):
    min_i = min(pattern, key=lambda n: n[0])[0]
    max_i = max(pattern, key=lambda n: n[0])[0]
    min_j = min(pattern, key=lambda n: n[1])[1]
    max_j = max(pattern, key=lambda n: n[1])[1]
    return (min_i, max_i, min_j, max_j)


def extract_mask(min_i, max_i, min_j, max_j, pattern):
    i = max_i - min_i + 1
    j = max_j - min_j + 1
    mask = [[0 for _ in range(j)] for _ in range(i)]
    for i, j in pattern:
        mask[i - min_i][j - min_j] = 1
    mask = tuple([tuple(m) for m in mask])
    return mask


def count_patterns(grid):
    stars = parse(grid)
    patterns = detect_patterns(stars)
    seen = set()
    c = 0

    for pattern in patterns:
        bounds = compute_bounds(pattern)
        mask = extract_mask(*bounds, pattern)
        if mask in seen:
            continue
        c += 1
        seen.add(mask)
    return c


if __name__ == "__main__":
    grid = [
        "*.*",
        ".*.",
        "**.",
    ]
    print(count_patterns(grid))  # 2

    grid = [
        "....*..*",
        "*.......",
        "......*.",
        "..*.....",
        "......*.",
    ]
    print(count_patterns(grid))  # 1

    grid = [
        "***.*.**",
        ".*..*..*",
        ".*.***..",
        ".......*",
        "......**",
    ]
    print(count_patterns(grid))  # 4

    grid = [
        "***.***.",
        "..*...*.",
        "**..**..",
        "..*...*.",
        "**..**..",
    ]
    print(count_patterns(grid))  # 1
