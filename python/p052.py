def calculate():
    start = 1
    found = False

    while not found:
        start *= 10
        for i in range(1, int(start * 10 / 6)):
            found = True
            for j in range(2, 7):
                if not is_perm(i, i*j):
                    found = False
                    break
            if found:
                return str(i)


def is_perm(x, y):
    return sorted(str(x)) == sorted(str(y))


if __name__ == "__main__":
    print(calculate())
