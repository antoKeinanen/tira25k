from timeit import default_timer as timer

n = 10**5

if __name__ == "__main__":
    lista = []
    alku = timer()

    for i in range(1, n + 1):
        lista.append(i)

    print("Lisäys:", timer() - alku)

    alku = timer()
    while len(lista) > 0:
        lista.pop()
    print("Poisto:", timer() - alku)