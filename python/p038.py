def calculate():
    largest = 0
    # Cap at 4 digits, since n > 1, and when n is 2, a 5+ digit num will go to a 10+ digit number
    for i in range(1, 10000):
        product = ""
        n = 1
        while len(product) < 9:
            product += str(i * n)
            n += 1
        if len(product) == len(set(product)) == 9 and "0" not in product:
            if int(product) > largest:
                largest = int(product)

    return str(largest)


if __name__ == "__main__":
    print(calculate())
