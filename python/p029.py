def calculate():
    powers = set(a**b for a in range(2, 101) for b in range(2, 101))
    return str(len(powers))


if __name__ == "__main__":
    print(calculate())
