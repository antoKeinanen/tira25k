import re
import itertools


class Oracle:
    def __init__(self, code):
        self.code = code
        self.counter = 0

    def check_code(self, code):
        self.counter += 1
        if self.counter > 16:
            raise RuntimeError("too many check_code calls")

        if (
            type(code) != str
            or not re.match("^[1-9]{4}$", code)
            or len(code) != len(set(code))
        ):
            raise RuntimeError("invalid code for check_code")

        in_place = in_code = 0
        for pos in range(4):
            if code[pos] in self.code:
                if code[pos] == self.code[pos]:
                    in_place += 1
                else:
                    in_code += 1

        return in_place, in_code


def find_code(oracle):
    def simulate_check(guess, code):
        in_place = in_code = 0
        for pos in range(4):
            if guess[pos] in code:
                if guess[pos] == code[pos]:
                    in_place += 1
                else:
                    in_code += 1

        return in_place, in_code
    
    codes = [
        "".join(c)
        for c in itertools.product("123456789", repeat=4)
        if len(set(c)) == len(c)
    ]

    while len(codes) > 0:
        guess = codes.pop()
        in_place, in_code = oracle.check_code(guess)
        if in_place == 4:
            return guess

        new_codes = []
        for code in codes:
            simulated = simulate_check(code, guess)
            if simulated == (in_place, in_code):
                new_codes.append(code)
        codes = new_codes



if __name__ == "__main__":
    oracle = Oracle("5631")
    code = find_code(oracle)
    print(code)  
