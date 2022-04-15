import itertools
import euler


def calculate():
    truncates = [37, 797, 3797]  # Given in question

    for i in itertools.count(10):
        if len(truncates) >= 11:
            return str(sum(truncates))
        if is_truncatable(i) and i not in truncates:
            truncates.append(i)


def is_truncatable(n):
    # Left
    i = 10
    while i <= n:
        if not euler.is_prime(n % i):
            return False
        i *= 10

    # Right
    while n > 0:
        if not euler.is_prime(n):
            return False
        n //= 10
    return True


if __name__ == "__main__":
    print(calculate())
