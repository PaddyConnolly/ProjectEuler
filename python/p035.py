import euler


def calculate():
    primes = euler.list_if_prime(999999)

    def is_circular(n):
        return all(primes[int(str(n)[i:] + str(n)[: i])] for i in range(len(str(n))))

    return str(sum(
        1 for i in range(len(primes))
        if is_circular(i)))


if __name__ == "__main__":
    print(calculate())
