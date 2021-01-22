def factOrSum(x, word):

    total = 1

    if word == "factorial":
        for i in range (1, x + 1):
            total = total * i

        return total

    else:

        total = 0

        for i in range (0, x + 1):
            total = total + i

    return total

print(factOrSum(5, "sum"))