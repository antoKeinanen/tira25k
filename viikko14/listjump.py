# https://cses.fi/tira25k/task/3553 

def find_steps(numbers):
    # TODO

if __name__ == "__main__":
    print(find_steps([1, 1, 1, 1])) # 3
    print(find_steps([3, 2, 1])) # -1
    print(find_steps([3, 5, 2, 2, 2, 3, 5])) # 10
    print(find_steps([7, 5, 3, 1, 4, 2, 4, 6, 1])) # 32

    numbers = []
    for i in range(10**5):
        numbers.append(1337 * i % 100 + 1)
    print(find_steps(numbers)) # 100055
