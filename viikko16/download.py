# https://cses.fi/tira25k/task/3563 

class Download:
    def __init__(self, n):
        # TODO

    def add_link(self, a, b, x):
        # TODO

    def max_data(self, a, b):
        # TODO

if __name__ == "__main__":
    download = Download(4)

    print(download.max_data(1, 4)) # 0

    download.add_link(1, 2, 5)
    download.add_link(2, 4, 6)
    download.add_link(1, 4, 2)
    print(download.max_data(1, 4)) # 7

    download.add_link(1, 3, 4)
    download.add_link(3, 2, 2)
    print(download.max_data(1, 4)) # 8
