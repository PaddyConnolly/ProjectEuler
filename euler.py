import math

# Useful functions for Project Euler


def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


def lcm(n):
    # The LCM (Lowest Common Multiple) of two  numbers x and y is given by LCM(x, y) = x * y / GCD(x, y), where GCD is the Greastest Common Divisor
    ans = 1
    for i in range(1, n + 1):
        ans *= i // math.gcd(i, ans)
    return ans


def euclid(m, n):
    return [m*m-n*n, 2*m*n, m*m+n*n]


def sum_divisors(n):
    total = 1
    root = int(math.sqrt(n))
    for i in range(2, root + 1):

        if n % i == 0:
            total += i
            total += n / i

    if n == root * root:
        total -= root

    return int(total)


def is_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True


def list_if_prime(n):
    # Sieve of Eratosthenes
    p = [True] * (n + 1)
    p[0] = p[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if p[i]:
            for j in range(i * i, len(p), i):
                p[j] = False
    return p


def ncr(n, r):
    return (math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))
