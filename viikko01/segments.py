def find_segments(data):
    prev = None
    n = 1
    buf = []
    
    for c in data:
        if prev is None:
            prev = c
            continue
        
        if c == prev:
            n += 1
            continue

        buf.append((n, prev))
        prev = c
        n = 1

    buf.append((n, prev))

    return buf 

if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]