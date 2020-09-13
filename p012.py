import math
import itertools


def calculate():

    def count_divisors(x):
        count = 0
        root = int(math.sqrt(x))
        for i in range(1, root):
            if x % i == 0:
                count += 2
        if x == root * root:
            count -= 1
        return count

    triangle = 0
    for i in itertools.count(1):
        triangle += i
        if count_divisors(triangle) > 500:
            return str(triangle)


if __name__ == "__main__":
    print(calculate())
