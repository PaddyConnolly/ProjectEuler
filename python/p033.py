import math


def calculate():
    # numerator < denominator
    # For the fraction 12 / 34, n1 = 1, n2 = 2, d1 = 3, d2 = 4
    # We dont consider fractions like 30 / 50, so we only need to check if n1 = d2 or n2 = d1
    final_n = 1
    final_d = 1
    for d in range(10, 100):
        for n in range(10, d):
            n1 = n // 10
            n2 = n % 10
            d1 = d // 10
            d2 = d % 10
            # Check if (incorrectly) cancellable, and if it would be correct
            if (n1 == d2 and n2 * d == d1 * n) or (n2 == d1 and n1 * d == d2 * n):
                final_n *= n
                final_d *= d
    return str(final_d // math.gcd(final_n, final_d))


if __name__ == "__main__":
    print(calculate())
