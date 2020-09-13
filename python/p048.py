def calculate():

    return str(sum(i ** i % 10**10 for i in range(1, 1001)) % 10**10)


if __name__ == "__main__":
    print(calculate())
