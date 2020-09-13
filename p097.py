def calculate():
    ans = (28433 * pow(2, 7830457, 10**10) + 1) % 10**10
    return str(ans)


if __name__ == "__main__":
    print(calculate())
