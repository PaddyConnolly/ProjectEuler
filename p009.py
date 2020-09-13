import euler
import numpy as np


def calculate():
    for x in range(1, 30):
        for y in range(1, 30):
            if sum(euler.euclid(x, y)) == 1000:
                return str(np.prod(euler.euclid(x, y)))


if __name__ == "__main__":
    print(calculate())
