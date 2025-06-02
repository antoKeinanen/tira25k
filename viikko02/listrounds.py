def find_rounds(numbers):
    c = []
    x = 0
    while len(numbers) > 0:
        d = []
        for n in numbers:
            if n == x + 1:
                d.append(n)
                x = n
        for n in d:
            numbers.remove(n)
        c.append(d)
    return c



if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]