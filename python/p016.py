def calculate():
    s = [int(x) for x in str(2**1000)]
    total = 0
    for item in s:
        total += item
    return str(total)


if __name__ == "__main__":
    print(calculate())
