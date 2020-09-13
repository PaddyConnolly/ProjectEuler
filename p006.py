def calculate():

    s1 = sum([i for i in range(1, 101)])
    s2 = sum([i * i for i in range(1, 101)])
    return str(s1**2 - s2)


if __name__ == "__main__":
    print(calculate())
