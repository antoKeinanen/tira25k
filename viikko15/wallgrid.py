class WallGrid:
    def __init__(self, n):
        self.n = n
        self.link = {}
        self.size = {}
        self.grid = set()
        self.rooms = 0

    def find(self, pos):
        if self.link[pos] != pos:
            self.link[pos] = self.find(self.link[pos])
        return self.link[pos]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False

        if self.size[ra] < self.size[rb]:
            self.link[ra] = rb
        else:
            self.link[rb] = ra
            if self.size[ra] == self.size[rb]:
                self.size[ra] += 1

        return True

    def create_floor(self, x, y):
        pos = (x, y)
        if pos in self.grid:
            return

        self.grid.add(pos)
        self.link[pos] = pos
        self.size[pos] = 0
        self.rooms += 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            npos = (nx, ny)
            if 1 <= nx <= self.n and 1 <= ny <= self.n and npos in self.grid:
                if self.union(pos, npos):
                    self.rooms -= 1

    def count_rooms(self):
        return self.rooms


if __name__ == "__main__":
    wall_grid = WallGrid(5)

    print(wall_grid.count_rooms())  # 0

    wall_grid.create_floor(2, 2)
    wall_grid.create_floor(4, 2)
    print(wall_grid.count_rooms())  # 2

    wall_grid.create_floor(3, 2)
    print(wall_grid.count_rooms())  # 1

    wall_grid.create_floor(2, 4)
    wall_grid.create_floor(2, 4)
    wall_grid.create_floor(4, 4)
    print(wall_grid.count_rooms())  # 3

    wall_grid.create_floor(3, 3)
    print(wall_grid.count_rooms())  # 3

    wall_grid.create_floor(3, 4)
    print(wall_grid.count_rooms())  # 1
