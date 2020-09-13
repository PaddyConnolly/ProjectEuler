def calculate():

    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day = 0
    count = 0

    for year in range(1901, 2001):
        for month in range(0, 12):
            day += months[month]
            if year % 4 == 0 and month == 28:
                day += 1
            if day % 7 == 0:
                count += 1

    return str(count)


if __name__ == "__main__":
    print(calculate())
