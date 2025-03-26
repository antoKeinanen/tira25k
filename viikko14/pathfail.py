# https://cses.fi/tira25k/task/3556 

class BellmanFord:
    # voit kopioida tämän luokan kurssimateriaalista

class Dijkstra:
    # voit kopioida tämän luokan kurssimateriaalista

def create_edges(n, a, b):
    # TODO

def find_answer(my_class, n, edges):
    nodes = range(1, n + 1)
    finder = my_class(nodes)

    for edge in edges:
        finder.add_edge(edge[0], edge[1], edge[2])

    distances = finder.find_distances(1)
    return distances[n]

if __name__ == "__main__":
    n = 100
    edges = create_edges(n, 42, 1337)

    answer1 = find_answer(BellmanFord, n, edges)
    print(answer1) # 42

    answer2 = find_answer(Dijkstra, n, edges)
    print(answer2) # 1337
