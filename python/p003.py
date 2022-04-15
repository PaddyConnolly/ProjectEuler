import euler


def calculate():
    n = 600851475143
    return str(euler.largest_prime_factor(n))


if __name__ == "__main__":
    print(calculate())
