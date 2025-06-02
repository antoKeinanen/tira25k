class CoursePlan:
    def __init__(self):
        self.nodes = {}

    def add_course(self, course):
        self.nodes[course] = []

    def add_requisite(self, course1, course2):
        self.nodes[course1].append(course2)

    def visit_node(self, node):
        if self.state[node] == 1:
            self.cycle = True
            return
        if self.state[node] == 2:
            return
        
        self.state[node] = 1
        for next_node in self.nodes[node]:
            self.visit_node(next_node)
        
        self.state[node] = 2
        self.order.append(node)

    def find_order(self):
        self.state = {}
        for node in self.nodes:
            self.state[node] = 0
        
        self.order = []
        self.cycle = False
        
        for node in self.nodes:
            if self.state[node] == 0:
                self.visit_node(node)
        
        if self.cycle:
            return None
        self.order.reverse()
        return self.order


if __name__ == "__main__":
    courses = CoursePlan()
    courses.add_course("Ohpe")
    courses.add_course("Ohja")
    courses.add_course("Tira")
    courses.add_course("Jym")

    courses.add_requisite("Ohpe", "Ohja")
    courses.add_requisite("Ohja", "Tira")
    courses.add_requisite("Jym", "Tira")

    print(courses.find_order()) # esim. [Ohpe, Jym, Ohja, Tira]

    courses.add_requisite("Tira", "Tira")

    print(courses.find_order()) # None
