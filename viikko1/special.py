def check_year(year):
    a, b = int(str(year)[0:2]), int(str(year)[2:4])
    return (a+b)**2 == year


if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False