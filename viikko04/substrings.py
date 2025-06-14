def count_substrings(string):
    b = set()
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            b.add(string[i:j])
    return len(b)


if __name__ == "__main__":
    print(count_substrings("aaaa"))  # 4
    print(count_substrings("abab"))  # 7
    print(count_substrings("abcd"))  # 10
    print(count_substrings("abbbbbb"))  # 13
    print(count_substrings("aybabtu"))  # 26
    print(count_substrings("saippuakauppias"))  # 110
