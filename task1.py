def sum1(a, b):
    a += 1
    if b == 1:
        return a
    return sum1(a, b - 1)


num = sum1(2, 2)
print(num)
