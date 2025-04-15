# https://cses.fi/tira25k/task/3567 

def min_changes(grid):
    # TODO

if __name__ == "__main__":
    grid = ["...#.",
            "...#.",
            "####.",
            ".....",
            "....."]

    print(min_changes(grid)) # 0

    grid = [".#...",
            "...#.",
            "...#.",
            ".###.",
            ".###."]

    print(min_changes(grid)) # 0

    grid = [".#...",
            "...#.",
            "...#.",
            ".###.",
            "....."]

    print(min_changes(grid)) # 1

    grid = [".....",
            ".###.",
            "...#.",
            "##.#.",
            "....."]

    print(min_changes(grid)) # 2
