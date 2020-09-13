import math


def calculate():
    number = [int(x) for x in str(math.factorial(100))]

    return str(sum(number))


if __name__ == "__main__":
    print(calculate())
