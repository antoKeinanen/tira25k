class MaxSet:
    def __init__(self, n):

        self.max = 1
        nodes = [i+1 for i in range(n)]
        self.link = {node: None for node in nodes}
        self.size = {node: 1 for node in nodes}
    
    def find(self, x):
        while self.link[x]:
            x = self.link[x]
        return x

    def merge(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return

        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]
        self.max = max(self.size[b], self.max)

    def get_max(self):
        return self.max