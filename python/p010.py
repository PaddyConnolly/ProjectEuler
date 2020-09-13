def calculate():
    n = 2_000_000
    array = [True for i in range(n + 1)]
    i = 2
    while (i * i <= n):

        if (array[i] == True):

            for j in range(i * 2, n + 1, i):
                array[j] = False
        i += 1
    array[0] = False
    array[1] = False
    output = []
    for prime in range(n + 1):
        if array[prime]:
            output.append(prime)

    return str(sum(output))


if __name__ == "__main__":
    print(calculate())
