
def atoi(input: str) -> int:
    res = 0

    for l in input:
        i = ord(l) - ord('0')
        res = res * 10 + i

    return res


print(atoi("124"))
