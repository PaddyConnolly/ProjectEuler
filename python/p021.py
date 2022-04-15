import math
import euler


def calculate():

    def d(x):

        return euler.sum_divisors(x)

    def amicable(a):
        if d(d(a)) == a and a != d(a):
            return True
        return False

    total = 0
    for a in range(2, 10001):
        if amicable(a):
            total += a

    return str(total)


if __name__ == "__main__":
    print(calculate())
