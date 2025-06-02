


if __name__ == "__main__":
    mf = MaximumFlow(range(1,8))
    edges = [
        (1, 2, 7),
        (2, 3, 3),
        (3, 7, 8),
        (2, 4, 2),
        (4, 3, 4),
        (4, 7, 3),
        (1, 5, 15),
        (5, 4, 3),
        (5, 6, 9),
        (6, 4, 5),
        (6, 7, 5)
    ]

    for edge in edges:
        mf.add_edge(*edge)
    
    print(mf.construct(1, 7))
