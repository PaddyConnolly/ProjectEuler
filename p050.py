import euler


def list_primes(n):
    return [i for (i, isprime) in enumerate(euler.list_if_prime(n)) if isprime]


def calculate():
    primes = list_primes(1000000)
    length = 0
    prev = len(primes)

    for i in range(len(primes)):
        for j in range(i + length, prev):
            solution = sum(primes[i:j])
            if solution < 1000000:
                if solution in primes:
                    length = j - i
                    largest = solution
            else:
                prev = j + 1
                break

# printing the requried solution
    return str(largest)


if __name__ == "__main__":
    print(calculate())
