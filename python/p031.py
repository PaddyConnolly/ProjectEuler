def calculate():
    TOTAL = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [1] + [0] * TOTAL  # add 1 to represent 0p

    for coin in coins:
        for i in range(coin, TOTAL + 1):
            ways[i] += ways[i - coin]
    return str(ways[-1])


if __name__ == "__main__":
    print(calculate())
