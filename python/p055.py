def calculate():

    count = 0
    for i in range(1, 10001):
        if is_lychrel(i):
            count += 1
    return str(count)


def is_lychrel(x):
    count = 0
    while count < 50:
        x += reverse(x)
        if not is_palindrome(x):
            count += 1
        else:
            return False

    return True


def is_palindrome(x):
    return reverse(x) == x


def reverse(x):
    n = 0
    while x > 0:
        n = n * 10 + x % 10
        x = x // 10
    return n


if __name__ == "__main__":
    print(calculate())
