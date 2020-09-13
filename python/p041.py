import euler


def calculate():
    # len(n) has to be 4 or 7, otherwise the digits will sum to a multiple of 3, which means it is divisible by 3
    n = 7654321
    while not (is_pandigital(n) and euler.is_prime(n)):
        n -= 2
    return str(n)


def is_pandigital(n):
    n = str(n)
    array = [str(x) for x in n]

    if sorted(array) == [str(x) for x in range(1, len(n) + 1)]:
        return True
    return False


if __name__ == "__main__":
    print(calculate())
