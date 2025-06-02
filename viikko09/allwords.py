import itertools
import re


def create_words(word):
    matcher = re.compile(r".*(.)\1.*")

    b = set()
    for c in itertools.permutations(word):
        c = "".join(c)
        if not matcher.match(c):
            b.add(c)
    return sorted(list(b))


if __name__ == "__main__":
    print(create_words("abc"))  # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create_words("aab"))  # ['aba']
    print(create_words("aaab"))  # []

    print(create_words("kala"))
    # ['akal', 'akla', 'alak', 'alka', 'kala', 'laka']

    print(create_words("syksy"))
    # ['ksysy', 'kysys', 'skysy', 'syksy', 'sykys', 'sysky',
    #  'sysyk', 'yksys', 'ysksy', 'yskys', 'ysyks', 'ysysk']

    print(len(create_words("aybabtu")))  # 660
    print(len(create_words("abcdefgh")))  # 40320
