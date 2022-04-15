import math


def calculate():
    n = 644
    count = 0

    while True:
        if prime_factors(n) == 4:
            if count == 0:
                answer = n
            count += 1
            if count == 4:
                return str(answer)

        else:
            answer, count = 0, 0
        n += 1


def prime_factors(n):
    count = 0
    while n > 1:
        count += 1
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                while True:
                    n //= i
                    if n % i != 0:
                        break
                break
        else:
            break
    return count


if __name__ == "__main__":
    print(calculate())
