def exponentiation(a, b):
    if b == 1:
        return a
    return a * exponentiation(a, b - 1)


num = exponentiation(int(input()), int(input()))
print(num)
