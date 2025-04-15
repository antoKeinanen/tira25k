# https://cses.fi/tira25k/task/3561 

class WallGrid:
    def __init__(self, n):
        # TODO

    def create_floor(self, x, y):
        # TODO

    def count_rooms(self):
        # TODO

if __name__ == "__main__":
    wall_grid = WallGrid(5)

    print(wall_grid.count_rooms()) # 0

    wall_grid.create_floor(2, 2)
    wall_grid.create_floor(4, 2)
    print(wall_grid.count_rooms()) # 2

    wall_grid.create_floor(3, 2)
    print(wall_grid.count_rooms()) # 1

    wall_grid.create_floor(2, 4)
    wall_grid.create_floor(2, 4)
    wall_grid.create_floor(4, 4)
    print(wall_grid.count_rooms()) # 3

    wall_grid.create_floor(3, 3)
    print(wall_grid.count_rooms()) # 3

    wall_grid.create_floor(3, 4)
    print(wall_grid.count_rooms()) # 1
