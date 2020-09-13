def calculate():
    string = "".join(str(i) for i in range(1, 1000000))
    output = 1
    for i in range(7):
        output *= int(string[10**i - 1])
    return str(output)


if __name__ == "__main__":
    print(calculate())
