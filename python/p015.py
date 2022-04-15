import math

# X must increase or Y must increase since no backtracking
# So 40 steps to reach finish (20 up or 20 across)
# So we need the amount of ways to choose 20 from a set of 40
# This can be written as 40C20 which is equivalent to
# 40! / 20! (40 - 20)! OR 40!/ 20!^2


def calculate():
    return str(int(math.factorial(40) / (math.factorial(20) * math.factorial(20))))


if __name__ == "__main__":
    print(calculate())
