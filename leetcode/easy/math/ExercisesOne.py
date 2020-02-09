from typing import List


def subtractProductAndSum2(n: int) -> int:
    as_str = str(n)
    sum = 0
    prod = 1
    for d in as_str:
        sum += int(d)
        prod *= int(d)
    return prod - sum


def subtractProductAndSum(n: int) -> int:
    sum = 0
    prod = 1
    while n > 0:
        d = n % 10
        sum += d
        prod *= d
        n = n // 10
    return prod - sum


print(subtractProductAndSum(234))


def maximum69Number(num: int) -> int:
    return int(str(num).replace('6', '9', 1))


print(maximum69Number(9669))


def selfDividingNumbers(left: int, right: int) -> List[int]:
    res = []
    for i in range(left, right + 1):
        if i < 10:
            res.append(i)
        else:
            add = True
            for n in (int(l) for l in str(i)):
                if n == 0 or i % n != 0:
                    add = False
                    break
            if add:
                res.append(i)

    return res


print(selfDividingNumbers(1, 22))


def diStringMatch(S: str) -> List[int]:
    length = len(S)
    min = 0
    max = length
    res = []
    for l in S:
        if l == 'I':
            res.append(min)
            min += 1
        else:
            res.append(max)
            max -= 1
    res.append(min)
    return res


print(diStringMatch("IDID"))
print(diStringMatch("DDI"))

