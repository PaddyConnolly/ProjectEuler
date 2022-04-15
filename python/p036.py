def calculate():
    return str(sum(i for i in range(1000000) if is_palindrome(i)))


def is_palindrome(n):
    decimal = str(n)
    if decimal != decimal[:: -1]:
        return False
    binary = bin(n)[2:]
    return binary == binary[:: -1]


if __name__ == "__main__":
    print(calculate())
