import euler
import itertools


def calculate():

    # Odd numbers starting from 9
    return str(next(filter(goldbach, itertools.count(9, 2))))


def goldbach(n):
    if n % 2 == 0 or euler.is_prime(n):
        return False
    for i in itertools.count(1):
        k = n - 2 * (i * i)
        if k <= 0:
            return True
        elif euler.is_prime(k):
            return False


if __name__ == "__main__":
    print(calculate())
