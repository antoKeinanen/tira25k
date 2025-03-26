# https://cses.fi/tira25k/task/3546 

class CountPaths:
    # voit kopioida tämän luokan kurssimateriaalista

def create_edges():
    # TODO

if __name__ == "__main__":
    edges = create_edges()

    counter = CountPaths(range(1, 100 + 1))
    for edge in edges:
        counter.add_edge(edge[0], edge[1])
    print(counter.count_paths(1, 100)) # 100
