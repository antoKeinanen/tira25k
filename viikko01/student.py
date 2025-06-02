B = [3, 7, 1, 3, 7, 1, 3, 7]

def check_number(number: str):
    if len(number) != 9:
        return False
    if number[0] != "0":
        return False
    
    l = int(number[-1])
    number = map(lambda c: int(c), number[0:8])
    c = sum([n*B[i] for i, n in enumerate(number)])
    
    return abs(c%10 - 10) % 10 == l
    


if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False