import math
import itertools


def calculate():
    for i in itertools.count():
        for j in range(1, i):
            a = i*(3*i-1)/2
            b = j*(3*j-1)/2
            if is_pentagonal(a+b) and is_pentagonal(a-b):
                return str(int(a-b))


def is_pentagonal(n):

    if (math.sqrt(24 * n+1) + 1) % 6 == 0:
        return True
    return False


if __name__ == "__main__":
    print(calculate())
