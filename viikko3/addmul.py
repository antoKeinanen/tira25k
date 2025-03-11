import re


def evaluate(data: str):
    add = set(re.findall("add\(([1-9][0-9]*),([1-9][0-9]*)\)", data))
    mul = set(re.findall("mul\(([1-9][0-9]*),([1-9][0-9]*)\)", data))
    for l, r in add:
        res = int(l) + int(r)
        data = data.replace(f"add({l},{r})", str(res))
    for l, r in mul:
        res = int(l) * int(r)
        data = data.replace(f"mul({l},{r})", str(res))
    return data


if __name__ == "__main__":
    print(evaluate("add(1,2)"))  # 3
    print(evaluate("aybabtu"))  # aybabtu
    print(evaluate("mul(6,7),mul(7,191)"))  # 42,1337
    print(evaluate("abadd(123,456)mulxmul(3,13)"))  # ab579mulx39
    print(evaluate("mul()mul(13)mul(0,1)"))  # mul()mul(13)mul(0,1)

    data = "mul(6,7)" * 10**5
    result = evaluate(data)
    print(len(result))  # 200000
    print(result[:20])  # 42424242424242424242
