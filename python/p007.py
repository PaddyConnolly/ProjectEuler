import euler


def calculate():

    # Old Code: 7.7s
    # n = 10001
    # primes = [2]
    # attempt = 3
    # while len(primes) < n:
    #     if all(attempt % prime != 0 for prime in primes):
    #         primes.append(attempt)
    #     attempt += 2
    # return str(primes[-1])

    # New Code: 0.1s
    def find_prime(n):
        count = 0
        prime = 1

        while count < n:
            prime += 1
            if euler.is_prime(prime):
                count += 1
        return prime

    return str(find_prime(10001))


if __name__ == "__main__":
    print(calculate())
