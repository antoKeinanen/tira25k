import re

def find_overlapping(string, word):
    return len(re.findall(f"(?={word})", string))

class WordFinder:
    def set_grid(self, grid):
        self.grid = list(map(lambda r: list(r), grid))
        self.w = len(grid[0])
        self.h = len(grid)
    



    def get_diagonals(self, word):
        n = 0
        for k in range(self.w + self.h - 1):
            s = ""
            for j in range(k + 1):
                i = k - j
                if i < self.h and j < self.w:
                    s += self.grid[i][j]
            n += find_overlapping(s, word) + find_overlapping(s[::-1], word)

        for k in range(self.h + self.w - 1):
            s = ""
            for i in range(max(0, k - self.w + 1), min(self.h, k + 1)):
                j = self.w - 1 - (k - i)
                s += self.grid[i][j]
            n += find_overlapping(s, word) + find_overlapping(s[::-1], word)
        return n

    def get_horizontal(self, word):
        n = 0
        for i in range(self.h):
            s = ""
            for j in range(self.w):
                s += self.grid[i][j]
            n += find_overlapping(s, word) + find_overlapping(s[::-1], word)
        return n

    def get_vertical(self, word):
        n = 0
        for j in range(self.w):
            s = ""
            for i in range(self.h):
                s += self.grid[i][j]
            n += find_overlapping(s, word) + find_overlapping(s[::-1], word)
        return n

    def count(self, word):
        n = 0
        n += self.get_horizontal(word)
        n += self.get_vertical(word)
        n += self.get_diagonals(word)

        if len(word) == 1:
            return n//8
        if word == word[::-1]:
            return n//2
        return n

if __name__ == "__main__":
    grid = ["TIRATIRA", "IRATIRAT", "RATIRATI", "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA"))  # 7
    print(finder.count("TA"))  # 13
    print(finder.count("RITARI"))  # 3
    print(finder.count("A"))  # 8
    print(finder.count("AA"))  # 6
    print(finder.count("RAITA"))  # 0
