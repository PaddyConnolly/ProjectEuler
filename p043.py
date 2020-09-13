import itertools


def calculate():
    solutions = []
    for n in itertools.permutations(list(range(10))):
        if is_divisible(n):
            solutions.append(int("".join(map(str, n))))
    return str(sum(solutions))


def is_divisible(n):
    TEST = [2, 3, 5, 7, 11, 13, 17]
    return all((n[i + 1] * 100 + n[i + 2] * 10 + n[i + 3]) % p == 0
               for (i, p) in enumerate(TEST))


if __name__ == "__main__":
    print(calculate())
