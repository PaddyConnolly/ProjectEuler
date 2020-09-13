def calculate():

    a = 286
    b = 166
    c = 144

    while True:
        triangle = a * (a + 1) // 2
        pentagon = b * (b * 3 - 1) // 2
        hexagon = c * (c * 2 - 1)
        smallest = min(triangle, pentagon, hexagon)
        if smallest == max(triangle, pentagon, hexagon):
            return str(triangle)
        if smallest == triangle:
            a += 1
        if smallest == pentagon:
            b += 1
        if smallest == hexagon:
            c += 1


if __name__ == "__main__":
    print(calculate())
