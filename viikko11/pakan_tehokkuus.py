from collections import deque
from timeit import default_timer as timer


def lisaa(pakka: deque, n: int):
    for i in range(1, n + 1):
        pakka.append(i)


def poista(pakka: deque):
    while len(pakka) > 0:
        pakka.popleft()


if __name__ == "__main__":
    pakka = deque()
    lisays_alkaa = timer()
    lisaa(pakka, 10**5)
    print("Lisäys valmis", timer() - lisays_alkaa)
    poisto_alkaa = timer()
    poista(pakka)
    print("Poisto valmis", timer() - poisto_alkaa)
