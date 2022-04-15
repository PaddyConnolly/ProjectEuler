def calculate():
    fibo = [1, 2]

    while fibo[-1] < 4_000_000:
        fibo.append(fibo[-1] + fibo[-2])
    fibo.pop()

    even_fibo = []
    for item in fibo:
        if item % 2 == 0:
            even_fibo.append(item)

    return str(sum(even_fibo))


if __name__ == "__main__":
    print(calculate())
