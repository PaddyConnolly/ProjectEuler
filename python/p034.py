import math


def calculate():

    # 8 * 9! isn't an 8 digit number, so we cap the loop at 7 digits
    return str(sum(i for i in range(3, 10000000) if i == sum_digits(i)))


def sum_digits(n):
    result = 0
    for char in str(n):
        result += math.factorial(int(char))
    return result


if __name__ == "__main__":
    print(calculate())
