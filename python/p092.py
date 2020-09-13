
def compute():
    total = 0
    for i in range(1, 10_000_000):
        total += count(i)
        print(i)
    return str(total)


eighty_nine = [89]
one = [1]

SQUARE_DIGITS = [sum(int(char)**2 for char in str(i)) for i in range(1000)]


def count(n):
    cache = []
    while True:
        if n in eighty_nine:
            for i in cache:
                eighty_nine.append(i)
            return 1
        elif n in one:
            for i in cache:
                eighty_nine.append(i)
            return 0
        else:
            cache.append(n)
            n = square_digit_sum(n)


def square_digit_sum(n):
    result = 0
    while n > 0:
        result += SQUARE_DIGITS[n % 1000]
        n //= 1000
    return result


if __name__ == "__main__":
    print(compute())
