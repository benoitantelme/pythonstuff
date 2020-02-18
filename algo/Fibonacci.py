from math import sqrt


def fibo(n: int) -> int:
    a = 0
    b = 1

    if n == 0:
        return a
    if n == 1:
        return b

    for i in range(2, n + 1):
        tmp = b
        b = a + b
        a = tmp

    return b


print(fibo(4))
print(fibo(8))


def fiboRecu(a: int, b: int, n: int, total: int) -> int:
    tmp = b
    b = a + b
    a = tmp

    if n == total:
        return b
    else:
        return fiboRecu(a, b, n + 1, total)


def fiboRec(n: int) -> int:
    if n == 1:
        return 0
    if n == 1:
        return 1

    return fiboRecu(0, 1, 2, n)


print(fiboRec(4))
print(fiboRec(8))


def fiboFormula(n: int) -> int:
    phi = (1 + sqrt(5)) / 2
    return round(pow(phi, n) / sqrt(5))


print(fiboFormula(4))
print(fiboFormula(8))
