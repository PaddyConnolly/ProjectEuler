import math


def calculate():
    # capped at 4 digits, since 5 digits makes the max possible product 99 * 99, which is doesn't reach 5 digits
    return str(sum(i for i in range(1, 10000) if pandigital_product(i)))


def pandigital_product(n):
    for i in range(1, int(math.sqrt(n)) + 1):
        if not n % i:
            string = str(n) + str(i) + str(n // i)
            if "".join(sorted(string)) == "123456789":
                return True
    return False


if __name__ == "__main__":
    print(calculate())
