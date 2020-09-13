import euler


def calculate():
    MAX = 10000
    primes = euler.list_if_prime(MAX - 1)
    for i in range(1000, 10000):
        if primes[i]:
            for step in range(1, MAX):
                a = i
                b = a + step
                c = b + step
                if b < MAX and primes[b] and has_same_digits(a, b) and c < MAX and primes[c] and has_same_digits(a, c) and a != 1487:
                    return str(a) + str(b) + str(c)


def has_same_digits(x, y):
    return sorted(str(x)) == sorted(str(y))


if __name__ == "__main__":
    print(calculate())
