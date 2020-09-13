import euler
import itertools
import math


def calculate():

    ans = max(((a, b) for a in range(-999, 1000, 2) for b in range(2, 1000)),  # B must be prime since n = 0 has to give us a prime
              key=count_primes)  # A must be odd since 1 + a + b where b is a prime must give us a prime
    return str(ans[0] * ans[1])


def count_primes(pair):
    a, b = pair
    for n in itertools.count():
        quadratic = (n ** 2) + (a * n) + b
        if not is_prime(quadratic):
            return n


cache = euler.list_if_prime(1000)


def is_prime(n):

    if n < 0:
        return False
    elif n < len(cache):
        return cache[n]
    else:
        return euler.is_prime(n)


if __name__ == "__main__":
    print(calculate())
