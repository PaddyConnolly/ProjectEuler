def calculate():
    highest = 10
    num = 1_000_000
    start = 1
    cache = [-1] * num
    cache[1] = 1

    for i in range(2, num):
        x = i
        count = 0
        while x != 1 and x >= i:
            count += 1
            if not x % 2:
                x /= 2
            else:
                x = x * 3 + 1

        cache[i] = count + cache[int(x)]

        if cache[i] > highest:
            highest = cache[i]
            start = i

    return str(start)


if __name__ == "__main__":
    print(calculate())
