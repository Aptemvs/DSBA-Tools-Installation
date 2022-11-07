n = int(input())
a = int(input())


def sqrt(num):
    return num ** 0.5


def square_sum(a, n, temp):
    if temp == n:
        return sqrt(a * n)
    return sqrt(a * temp + square_sum(a, n, temp + 1))


print(square_sum(a, n, 1))
