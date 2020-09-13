import math


def calculate():
    LIMIT = 1000
    n = 3
    d = 2
    count = 0

    for _ in range(LIMIT):
        n += 2 * d
        d = n - d
        if len(str(n)) > len(str(d)):
            count += 1

    return str(count)


if __name__ == "__main__":
    print(calculate())
