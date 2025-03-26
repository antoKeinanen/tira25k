# https://cses.fi/tira25k/task/3547 

class CountPaths:
    # voit kopioida tämän luokan kurssimateriaalista

def create_edges(x):
    # TODO

if __name__ == "__main__":
    edges = create_edges(123456789)

    counter = CountPaths(range(1, 100 + 1))
    for edge in edges:
        counter.add_edge(edge[0], edge[1])
    print(counter.count_paths(1, 100)) # 123456789
