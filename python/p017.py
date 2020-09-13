def calculate():

    # 1 - 9

    total = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4  # = 36

    # 10 - 19

    total += 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8  # = 70

    # 20 - 99

    total += 10 * (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6)  # Prefix
    total += 8 * 36  # Suffix  = 748

    # Total = 854

    # 100 to 999

    total += 36 * 100  # Prefix appears 100 times each
    total += 9 * 854  # 1 - 99 appears 9 times each
    total += 9 * 7  # Hundred appears 9 times on its own
    total += 891 * 10  # And 891 times with "hundred and"
    total += 11  # one thousand

    return str(total)


if __name__ == "__main__":
    print(calculate())
