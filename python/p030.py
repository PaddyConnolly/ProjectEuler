def calculate():
    # Limits at 6 digits since 7 * (9 ** 5) is 6 digits, so you can never make a 7 digit number
    answer = sum(x for x in range(2, 1000000) if x == sum_digits(x))
    return str(answer)


def sum_digits(n):
    return sum(int(x)**5 for x in str(n))


if __name__ == "__main__":
    print(calculate())
