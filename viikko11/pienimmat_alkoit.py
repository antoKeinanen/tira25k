import heapq
from random import randint
from timeit import default_timer as timer


def algoritmi_1(n: int):
    lista = [randint(1, 10**9) for _ in range(n)]

    sorted(lista)
    return sum(lista[: n // 10])


def algoritmi_2(n: int):
    lista = []
    for _ in range(n):
        heapq.heappush(lista, randint(1, 10**9))
    return sum(heapq.nsmallest(n // 10, lista))


def algoritmi_3(n: int):
    lista = [randint(1, 10**9) for _ in range(n)]
    heapq.heapify(lista)
    return sum(heapq.nsmallest(n // 10, lista))


if __name__ == "__main__":
    n = 10**7

    alku = timer()
    tulos = algoritmi_1(n)
    print("Algoritmi 1 valmis", tulos, timer() - alku)

    alku = timer()
    tulos = algoritmi_2(n)
    print("Algoritmi 2 valmis", tulos, timer() - alku)

    alku = timer()
    tulos = algoritmi_3(n)
    print("Algoritmi 3 valmis", tulos, timer() - alku)
