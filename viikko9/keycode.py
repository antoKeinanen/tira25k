import copy

def find_codes(pattern: str):
    codes = []

    if pattern.isdigit():
        return [pattern]

    for i in range(len(pattern)):
        ch = pattern[i]
        if ch == "?":
            for j in range(1, 10):
                if str(j) in pattern:
                    continue
                new_pattern = list(pattern)
                new_pattern[i] = str(j)
                new_pattern = "".join(new_pattern)
                codes.extend(find_codes(new_pattern))
    return sorted(list(set(codes)))

if __name__ == "__main__":
    codes = find_codes("24?5")
    print(codes) # ['2415', '2435', '2465', '2475', '2485', '2495']

    codes = find_codes("1?2?")
    print(codes[:5]) # ['1324', '1325', '1326', '1327', '1328']
    print(len(codes)) # 42

    codes = find_codes("????")
    print(codes[:5]) # ['1234', '1235', '1236', '1237', '1238']
    print(len(codes)) # 3024