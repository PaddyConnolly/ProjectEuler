import math


def calculate():

    # 10! = 3 628 800 Number of total permutations
    # Therefore there are 362 880 permuations beginning with 0, beginning with 1, etc.
    # Therefore the 1 millionth permutation is the 274 240th permuatation beginning with a 2
    # We can go through the same process again, 9! perms left, which means 40320 with 20, with 21, with 22, etc.
    # Therefore the 274 240 th permutation beginning with a 2 starts with 26 (not 5 since 2 is already used), and is the 32 320th permutation starting with 26
    # 32 020 -> 8! = 40320 -> 5040 each -> 267 -> 1780th -> 7! = 5040 -> 720 each -> 2671 -> 340 th -> 6! = 720 => 120 each -> 26713 -> 100th -> 5! = 120 = 24 each 267138 4 th -> 4! = 24 = 6 each -> 1

    place = 1_000_000
    output = []
    array = [str(x) for x in range(0, 10)]
    count = 1
    while len(array) > 1:
        perms_each = math.factorial(len(array) - 1)
        index = (place // perms_each)
        remainder = place - (index * perms_each)
        if remainder == 0:
            index -= 1
        output.append(array[index])
        array.pop(index)
        place = remainder
        count += 1
    output.append(array[0])

    return "".join(output)


if __name__ == "__main__":
    print(calculate())
