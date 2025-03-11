from timeit import default_timer as timer
from random import randint


# toteutus 1
def count_even1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result


# toteutus 2
def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)


def prep_random_list(count):
    return [randint(1, 9) for _ in range(count)]


if __name__ == "__main__":
    list1 = prep_random_list(10**7)
    start1 = timer()
    count_even1(list1)
    end1 = timer()
    
    print(1, end1 - start1)

    list2 = prep_random_list(10**7)
    start2 = timer()
    count_even2(list2)
    end2 = timer()

    print(2, end2 - start2)
