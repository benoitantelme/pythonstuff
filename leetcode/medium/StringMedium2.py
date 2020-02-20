import re


def addXs(part) -> int:
    res = 0

    for m in [m for m in part if 'x' in m]:
        if len(m) == 0:
            continue

        minus = False
        if m[0] == '-':
            minus = True
            m = m[1:]
        elif m[0] == '+':
            m = m[1:]

        if m == 'x':
            if minus:
                res -= 1
            else:
                res += 1
        else:
            val = int(m[:-1])
            if minus:
                res -= val
            else:
                res += val
    return res


def addNums(part) -> int:
    res = 0

    for m in [m for m in part if 'x' not in m]:
        if len(m) == 0:
            continue

        minus = False
        if m[0] == '-':
            minus = True
            m = m[1:]
        elif m[0] == '+':
            m = m[1:]

        val = int(m)
        if minus:
            res -= val
        else:
            res += val

    return res


def solveEquation(equation: str) -> str:
    parts = equation.split('=')
    left = parts[0]
    right = parts[1]

    pattern = "([-+]?[0-9]*[x]?)"
    lsplit = re.findall(pattern, left)
    rsplit = re.findall(pattern, right)

    xs = 0
    xs += addXs(lsplit)
    xs -= addXs(rsplit)

    nums = 0
    nums -= addNums(lsplit)
    nums += addNums(rsplit)

    if xs == 0:
        if nums == 0:
            return 'Infinite solutions'
        else:
            return 'No solution'
    elif xs == 1:
        if nums != 0:
            return 'x=' + str(nums)
        else:
            return 'x=0'
    else:
        return 'x=' + str(nums // xs)


print(solveEquation("x=3"))
print(solveEquation("2x=x"))
print(solveEquation("2x+3x-6x=x+2"))
print(solveEquation("x=x"))
print(solveEquation("x=x+2"))

