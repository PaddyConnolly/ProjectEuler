def calculate():

    product = max([x * y
                   for x in range(100, 1000)
                   for y in range(100, 1000)
                   if str(x * y) == str(x * y)[::-1] and x*y % 11 == 0])

    return str(product)


if __name__ == "__main__":
    print(calculate())
