class Contest:
    def __init__(self, names, task_count):
        self.scores = sorted([(name, [0] * task_count, 0) for name in names])
        print(self.scores)

    def add_submission(self, name, task, score):
        person = list(filter(lambda s: s[0] == name, self.scores))[0]
        self.scores.remove(person)
        s = person[1][task - 1]
        person[1][task - 1] = max(s, score)
        person = (person[0], person[1], sum(person[1]))
        for i, c in enumerate(self.scores):
            if person[2] > c[2]:
                self.scores.insert(i, person)
                break
        print(self.scores)

    def create_scoreboard(self):
        return list(map(lambda s: (s[0], sum(s[1])), self.scores))


if __name__ == "__main__":
    names = ["anna", "pekka", "kalle", "tiina", "eeva"]
    contest = Contest(names, 3)

    contest.add_submission("tiina", 2, 30)
    contest.add_submission("pekka", 1, 40)
    contest.add_submission("tiina", 1, 20)
    contest.add_submission("pekka", 1, 50)
    contest.add_submission("pekka", 2, 0)
    contest.add_submission("eeva", 3, 100)
    contest.add_submission("anna", 1, 0)
    contest.add_submission("eeva", 3, 80)
    contest.add_submission("tiina", 2, 30)

    scoreboard = contest.create_scoreboard()
    print(scoreboard)
    # [('eeva', 100), ('tiina', 50), ('pekka', 50), ('anna', 0), ('kalle', 0)]
