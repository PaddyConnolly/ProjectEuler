import itertools


def calculate():

    DIGITS = 1000
    previous = 1
    current = 0
    for i in itertools.count():
        if len(str(current)) == DIGITS:
            return str(i)

        previous, current = current, previous + current


if __name__ == "__main__":
    print(calculate())
