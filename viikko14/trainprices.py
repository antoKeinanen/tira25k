class TrainPrices:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_city(self, name):
        self.nodes.append(name)
        self.nodes.sort()

    def add_train(self, city1, city2, price):
        self.edges.append((city1, city2, price))
        self.edges.append((city2, city1, price))

    def find_prices(self):
        table = [[None, *self.nodes]]
        for city1 in self.nodes:
            distances = {}
            for node in self.nodes:
                distances[node] = float("inf")
            distances[city1] = 0
            previous = {}
            previous[city1] = 0

            for _ in range(len(self.nodes) - 1):
                for edge in self.edges:
                    node_a, node_b, weight = edge
                    new_distance = distances[node_a] + weight
                    if new_distance < distances[node_b]:
                        distances[node_b] = new_distance
                        previous[node_b] = node_a
            
            distances = [-1 if dist == float("inf") else dist for dist in distances.values()] 
            table.append([city1, *distances])
        return table 


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
