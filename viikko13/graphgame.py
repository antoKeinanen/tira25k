class GraphGame:
    def __init__(self, n):
        self.nodes = [i + 1 for i in range(n)]
        self.graph = {node: [] for node in self.nodes}
 
    def add_link(self, a, b):
        self.graph[a].append(b)
    
 
    def evaluate(self, node, operator):
        if not self.graph[node]:
            if operator is max:
                return 0
            return 1
        
        if operator is max:
            return max([self.evaluate(n, min) for n in self.graph[node]])
        return min([self.evaluate(n, max) for n in self.graph[node]])
 
    def winning(self, x):
        return bool(self.evaluate(x, max))
 
 
if __name__ == "__main__":
    game = GraphGame(6)
 
    game.add_link(3, 4)
    game.add_link(1, 4)
    game.add_link(4, 5)
 
    print(game.winning(3)) # False
    print(game.winning(1)) # False
 
    game.add_link(3, 1)
    game.add_link(4, 6)
    game.add_link(6, 5)
 
    print(game.winning(3)) # True
    print(game.winning(1)) # False
    print(game.winning(2)) # False