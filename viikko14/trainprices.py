# https://cses.fi/tira25k/task/3552 

class TrainPrices:
    def __init__(self):
        # TODO

    def add_city(self, name):
        # TODO

    def add_train(self, city1, city2, price):
        # TODO

    def find_prices(self):
        # TODO

if __name__ == "__main__":
    prices = TrainPrices()

    prices.add_city("Helsinki")
    prices.add_city("Turku")
    prices.add_city("Tampere")
    prices.add_city("Oulu")

    prices.add_train("Helsinki", "Tampere", 20)
    prices.add_train("Helsinki", "Turku", 10)
    prices.add_train("Tampere", "Turku", 50)

    print(prices.find_prices())

    # metodin haluttu tulos:
    # [[None,       'Helsinki', 'Oulu', 'Tampere', 'Turku'],
    #  ['Helsinki', 0,          -1,     20,        10],
    #  ['Oulu',     -1,         0,      -1,        -1],
    #  ['Tampere',  20,         -1,     0,         30],
    #  ['Turku',    10,         -1,     30,        0]]
