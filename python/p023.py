import euler


def calculate():

    MAX = 28124

    def is_abundant(n):
        if euler.sum_divisors(n) > n:
            return True
        return False

    abundants = []
    for x in range(MAX):
        if is_abundant(x):
            abundants.append(x)

    array = [0] * MAX

    for x in range(1, len(abundants)):
        for y in range(x, len(abundants)):
            div_sum = abundants[x] + abundants[y]
            if div_sum < MAX:
                if array[div_sum] == 0:
                    array[div_sum] = div_sum

    total = 0
    for i in range(1, len(array)):
        if array[i] == 0:
            total += i

    return str(total)


if __name__ == "__main__":
    print(calculate())
