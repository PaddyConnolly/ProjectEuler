def calculate():
    # Top Right will always be n^2
    # Top Left will always be n^2 - (n-1)
    # Bottom Left will always be n^2 - 2(n-1)
    # Bottom Right will always be n^2 - 3(n-1)
    # Therefore the outermost ring will always sum to 4n^2 - 6(n-1)
    LENGTH = 1001
    answer = 1  # Start at 1 to include middle
    answer += sum(4 * i * i - 6 * (i - 1) for i in range(3, LENGTH + 1, 2))
    return str(answer)


if __name__ == "__main__":
    print(calculate())
