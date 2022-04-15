import euler


def calculate():

    count = 0

    for x in range(1, 101):
        for y in range(1, x+1):
            if(euler.ncr(x, y) > 1000000):
                count += 1

    return str(count)


if __name__ == "__main__":
    print(calculate())
