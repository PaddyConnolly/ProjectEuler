def calculate():
    return str(max(range(1, 1001), key=count_perimeter_solutions))


def count_perimeter_solutions(p):
    solutions = 0
    for a in range(1, p+1):
        for b in range(a, (p-a // 2) + 1):
            c = p - a - b
            if a * a + b * b == c * c:
                solutions += 1
    return solutions


if __name__ == "__main__":
    print(calculate())
