# https://cses.fi/tira25k/task/3565 

class Ball:
    def __init__(self, n):
        # TODO

    def add_pair(self, a, b):
        # TODO

    def max_pairs(self):
        # TODO

if __name__ == "__main__":
    ball = Ball(4)

    print(ball.max_pairs()) # 0

    ball.add_pair(1, 2)
    print(ball.max_pairs()) # 1

    ball.add_pair(1, 3)
    ball.add_pair(3, 2)
    print(ball.max_pairs()) # 2

    ball.add_pair(2, 1)
    print(ball.max_pairs()) # 3
