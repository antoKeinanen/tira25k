from math import comb
from fractions import Fraction


def count_sequences(n):
    if n % 2 != 0:
        return 0
    n2 = n//2
    return Fraction(1, n2+1) * comb(n, n2)


if __name__ == "__main__":
    print(count_sequences(1)) # 0
    print(count_sequences(2)) # 1
    print(count_sequences(3)) # 0
    print(count_sequences(4)) # 2
    print(count_sequences(5)) # 0
    print(count_sequences(6)) # 5

    print(count_sequences(42)) # 24466267020
    print(count_sequences(62))  # 14544636039226909
    print(count_sequences(1000)) # 539497486917039060909410566119711128734834348196703167679426896420410037336371644508208550747509720888947317534973145917768881736628103627844100238921194561723883202123256952806711505149177419849031086149939116975191706558395784192643914160118616272189452807591091542120727401415762287153293056320
