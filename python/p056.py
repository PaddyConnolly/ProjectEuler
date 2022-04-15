def calculate():
    return str(max(sum(map(int, str(a**b))) for a in range(100, 90, -1) for b in range(100, 90, -1)))


if __name__ == "__main__":
    print(calculate())
