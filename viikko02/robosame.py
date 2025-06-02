def calculate(input, rules):
    state = 1
    count = 1000
    index = 0
    input = list("L" + input + "R")

    while True:
        if count <= 0:
            print("INFINITE LOOP")
            return False

        ch = input[index]
        for rule in rules:
            if rule[0] == ch and rule[1] == state:
                if rule[4] == "RIGHT" and index == len(input) - 1:
                    print("RIGHT BOUND")
                    return False
                if rule[4] == "LEFT" and index == 0:
                    print("LEFT BOUND")
                    return False
                if rule[4] == "ACCEPT":
                    print("MANUAL ACCEPT")
                    return True
                if rule[4] == "REJECT":
                    print("MANUAL REJECT")
                    return False

                input[index] = rule[2]
                state = rule[3]
                count -= 1

                if rule[4] == "RIGHT":
                    index += 1
                if rule[4] == "LEFT":
                    index -= 1

                # print(rule)
                break

        else:
            print("NO RULE MATCH", state, index, input)
            return False

def create_rules():
    return [
        ("L", 1, "L", 0, "RIGHT"),
        ("0", 0, "L", 0, "RIGHT"),
    ]


if __name__ == "__main__":
    rules = create_rules()

    print(calculate("00", rules))  # True
    print(calculate("001001", rules))  # True
    print(calculate("10111011", rules))  # True
    print(calculate("01", rules))  # False
    print(calculate("00100", rules))  # False
    print(calculate("10111101", rules))  # False
